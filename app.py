from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database connection and setup
db = mysql.connector.connect(
    host='localhost',
    user='root',  # Change to your MySQL username
    password='helon@123',  # Change to your MySQL password
    database='school_emergency_sos'  # Change to your database name
)

# Create the students table if it doesn't exist
cursor = db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    admission_number VARCHAR(50) UNIQUE,
    contact_numbers TEXT  -- Comma-separated contact numbers
)
''')
db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    admission_number = request.form.get('admission_number')
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM students WHERE admission_number = %s"
    cursor.execute(query, (admission_number,))
    student = cursor.fetchone()

    cursor.close()

    if student:
        return render_template('result.html', student=student)
    else:
        return render_template('result.html', student=None)

if __name__ == '__main__':
    app.run(debug=True)