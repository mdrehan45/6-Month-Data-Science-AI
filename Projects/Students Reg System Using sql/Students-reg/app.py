from flask import Flask, render_template, request, redirect, flash, url_for
import mysql.connector

# Flash for msg and render_template for HTML pages and request for form data and url_for for URL building.
# mysql.connector for MySQL database connection.

app = Flask(__name__)
app.secret_key = 'my_name_is_rehan'

# creating flask app

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mdrehan@45',
        database="students"
    )

# redirecting to students route

@app.route('/')
def home():
    return redirect(url_for('students'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        course = request.form.get('course', '').strip()
        if not name or not email or not course:
            flash("All fields are required!", "danger")
            return render_template('register.html')
        try:
            db = get_db_connection()
            with db.cursor() as cursor:
                query = "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)"
                cursor.execute(query, (name, email, course))
                db.commit()
            flash("Student added successfully!", "success")
            return redirect(url_for('students'))
        except Exception as e:
            flash(f"Error: {e}", "danger")
        finally:
            db.close()
    return render_template('register.html')

# to show list of students
@app.route('/students')
def students():
    try:
        db = get_db_connection()
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM students")
            all_students = cursor.fetchall()
        return render_template('students.html', students=all_students)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return render_template('students.html', students=[])
    finally:
        db.close()

@app.route('/delete/<int:id>')
def delete(id):
    try:
        db = get_db_connection()
        with db.cursor() as cursor:
            cursor.execute("DELETE FROM students WHERE id = %s", (id,))
            db.commit()
        flash("Student deleted successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    finally:
        db.close()
    return redirect(url_for('students'))

@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    try:
        db = get_db_connection()
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
            student = cursor.fetchone()
        if not student:
            flash("Student not found!", "danger")
            return redirect(url_for('students'))
        return render_template('edit.html', student=student)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('students'))
    finally:
        db.close()

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    course = request.form.get('course', '').strip()
    if not name or not email or not course:
        flash("All fields are required!", "danger")
        return redirect(url_for('edit', id=id))
    try:
        db = get_db_connection()
        with db.cursor() as cursor:
            query = "UPDATE students SET name=%s, email=%s, course=%s WHERE id=%s"
            cursor.execute(query, (name, email, course, id))
            db.commit()
        flash("Student updated successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    finally:
        db.close()
    return redirect(url_for('students'))

@app.route('/dashboard')
def dashboard():
    try:
        db = get_db_connection()
        with db.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM students")
            total = cursor.fetchone()[0]
        return render_template('dashboard.html', total=total)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return render_template('dashboard.html', total=0)
    finally:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)