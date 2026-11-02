# Student Hub — Student Management System

A Flask and MySQL application for managing student records through a web dashboard or a console menu.

## Features

- Add, view, edit, and delete student records
- Search records by student name or ID
- Filter by mark range and sort by ID, name, age, or marks
- View student count, class average, and top mark at a glance
- See a visual marks bar for each student
- Validate names, ages, and marks before saving
- Confirm before deleting a record
- Enter the MySQL password in the terminal instead of storing it in source code
- Responsive layout for smaller screens

## Requirements

- Python 3
- MySQL Server

Install the packages from the project folder:

```bash
python -m pip install -r requirements.txt
```

## Database setup

Run this SQL in MySQL if you have not created the database and table yet:

```sql
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    marks INT NOT NULL
);
```

The default connection in `db_connection.py` uses `localhost`, the MySQL user `root`, and database `student_db`. Adjust the host or username there if your MySQL setup differs. The password is requested in the terminal and is not displayed while typing.

## Run the web app

From the project directory, activate your virtual environment, then run:

```bash
python app.py
```

Enter your MySQL password when prompted. Open the address printed in the terminal (currently `http://127.0.0.1:5001`). Keep the terminal open while using the app.

## Use the dashboard

- Use **Add student** to create a record.
- Search by a student's name or ID. Press **Ctrl+K** (or **⌘K**) to focus the search box; press **Escape** to clear it.
- Filter marks into 90+, 75–89, and below 75 ranges.
- Sort by ID, name, age, or marks.
- Use the edit action to update a record. The delete action asks for confirmation.

## Run the console menu

```bash
python main.py
```

## Project structure

```text
app.py
db_connection.py
student_operations.py
main.py
requirements.txt
templates/
  index.html
  add_student.html
  update_student.html
static/
  style.css
  dashboard.js
```

## Notes

- Age must be between 1 and 120; marks must be between 0 and 100.
- `app.py` uses Flask's development server. Do not expose it directly to the public internet or use it as a production server.
- Set a private Flask secret key and use a production WSGI server before deploying publicly.
