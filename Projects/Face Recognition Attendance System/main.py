import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Load known faces
path = 'ImagesAttendance'
images = []
names = []
# in this step we are loading the images from the folder and storing them in a list
for file in os.listdir(path):
    img = cv2.imread(f'{path}/{file}')
    if img is None:
        continue
    images.append(img)
    names.append(os.path.splitext(file)[0])   # Name without extension

# now we are encoding the images
def encode_faces(images):
    encodings = []
    for img in images:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_encs = face_recognition.face_encodings(img_rgb)
        if len(face_encs) > 0:   # Only take if face found
            encodings.append(face_encs[0])
    return encodings

#here we are encoding the faces
known_encodings = encode_faces(images)


# now we are creating a function to mark attendance. defining date and time
def markAttendance(name):
    today = datetime.now().strftime('%Y-%m-%d')
    now = datetime.now()
    dtString = now.strftime('%H:%M:%S')

    # Create file if not exists
    if not os.path.exists('Attendance.csv'):
        with open('Attendance.csv', 'w') as f:
            f.write("Name,Date,Time")

    with open('Attendance.csv', 'r+') as f:
        lines = f.readlines()
        nameList = [line.strip() for line in lines]

        # Check with date so multiple days attendance works
        record = f"{name},{today}"
        if not any(record in line for line in nameList):
            f.writelines(f"\n{name},{today},{dtString}")


# Webcam loop
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break
# here we are resizing the image and converting it to rgb 
    img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img_rgb = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(img_rgb)
    encodesCurFrame = face_recognition.face_encodings(img_rgb, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(known_encodings, encodeFace)
        faceDis = face_recognition.face_distance(known_encodings, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex] and faceDis[matchIndex] < 0.5:   # threshold check
            name = names[matchIndex].upper()
        else:
            name = "UNKNOWN"

        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # Scale back up
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, name, (x1 + 6, y2 + 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        if name != "UNKNOWN":
            markAttendance(name)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
