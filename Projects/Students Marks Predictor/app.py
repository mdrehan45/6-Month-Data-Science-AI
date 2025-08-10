from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("student_mark_predict.pkl")

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            hours = float(request.form['hours'])

            # Input validation
            if hours < 0 or hours > 24:
                return render_template('index1.html', error="❌ Study hours must be between 0 and 24.")

            # Make prediction
            prediction = model.predict([[hours]])[0][0].round(2)

            #predicted marks between 0 and 100
            prediction = max(0.0, min(100.0, prediction))

            # Save to CSV file
            new_row = pd.DataFrame({'Study Hours': [hours], 'Predicted Output': [prediction]})
            try:
                old_df = pd.read_csv('smp_data_from_app.csv')
                df = pd.concat([old_df, new_row], ignore_index=True)
            except Exception:
                df = new_row
            df.to_csv('smp_data_from_app.csv', index=False)

            return render_template('index1.html', prediction=prediction, hours=hours)

        except Exception as e:
            return render_template('index1.html', error=f"❌ Invalid input: {str(e)}")
    # If not POST, just render the template with no prediction
    return render_template('index1.html')

if __name__ == "__main__":
    app.run(debug=True)