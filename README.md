# soswebapp

## Overview
soswebapp is a web application designed to facilitate the search for student details using their admission number. The application uses Python with the Flask framework and a MySQL database to store student information.

## Features
- Search for student details using admission number.
- Display student details including name and contact numbers.
- Call functionality directly from the web interface.

## Project Structure
The main files in the repository are:
- `app.py`: The main Flask application file that handles routing and database interactions.
- `templates/index.html`: The HTML template for the search form.
- `templates/result.html`: The HTML template for displaying student details.

## Setup Instructions
To set up and run the soswebapp, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/basil-the-py-developer/soswebapp.git
   cd soswebapp
   ```
2. **Install dependencies:**
   Make sure you have Python and MySQL installed. Then, install the required Python packages:
   ```
   pip install flask mysql-connector-python
   ```
3. **Database setup:**
   Create a MySQL database and update the database configuration in app.py:
   ```sql
   CREATE DATABASE school_emergency_sos;
   USE school_emergency_sos;
   ```
4. **Run the application:**
   Start the Flask application:
   ```
   python app.py
   ```
5. **Access the application:**
   Open your web browser and go to http://127.0.0.1:5000/.
## Usage

### Search for a Student:

1. Navigate to the home page.
2. Enter the student's admission number in the search form.
3. Click the "Search" button to view the student's details.

### View Student Details:
- If the student is found, their details including name and contact numbers will be displayed.
- Click on the call button to initiate a phone call to the student's contact number.

