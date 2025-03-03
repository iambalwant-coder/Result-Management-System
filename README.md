# Student Management System (Django)

A simple Django-based web application to manage student records, including their marks, results, and personal details. This application allows adding, viewing, editing, and deleting student records, along with filtering students based on their name and result status.

## Features

- **Home Page**: Displays a list of all students.
  - Filter students by name and result status (PASS/FAIL).
- **Add Student**: Allows adding new student records with details like ID, name, marks in subjects (Math, Science, English), and calculates total marks and percentage.
- **Edit Student**: Allows editing existing student records, updating marks, and recalculating the result and percentage.
- **View Student**: Displays detailed information about a specific student.
- **Delete Student**: Allows deleting a student's record from the system.
- **About Page**: Displays information about the system.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Database**: SQLite (default for Django)

## Installation Instructions

### Step 1: Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/student-management-system.git
```

### Step 2: Set up a virtual environment

Create and activate a virtual environment to isolate dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Step 3: Install dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Migrate the database

Run the following command to create the necessary database tables:

```bash
python manage.py migrate
```

### Step 5: Create a superuser (optional)

To access the Django admin panel, you can create a superuser:

```bash
python manage.py createsuperuser
```

### Step 6: Run the development server

Start the Django development server:

```bash
python manage.py runserver
```

Now you can access the application in your browser at `http://127.0.0.1:8000/`.

## Usage

- **Home Page**: Lists all students with options to filter by name or result status.
- **Add Student**: Add a new student by navigating to the "Add Student" page.
- **Edit Student**: Update an existing student's details by clicking the "Edit" button next to the student's name.
- **View Student**: View a student's full details by clicking the "View" button.
- **Delete Student**: Remove a student from the system by clicking the "Delete" button.
- **About**: Learn more about the application on the About page.

## Project Structure

```
student_management_system/
│
├── student_management_system/  # Main project directory
│   ├── settings.py             # Django settings
│   ├── urls.py                 # URL configurations
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── students/                   # Student app directory
│   ├── models.py               # Database models for Student
│   ├── views.py                # Views for handling requests
│   ├── urls.py                 # URLs for the Student app
│   ├── templates/              # HTML templates
│   │   ├── home.html           # Home page template
│   │   ├── add.html            # Add student page template
│   │   ├── edit.html           # Edit student page template
│   │   ├── view.html           # View student details template
│   │   └── about.html          # About page template
│   └── migrations/             # Database migrations
│
├── manage.py                   # Django management script
├── requirements.txt            # List of required Python packages
└── README.md                   # Project documentation (this file)
```

## Models

### Student Model

```python
class Student(models.Model):
    student_id = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    math = models.IntegerField()
    science = models.IntegerField()
    english = models.IntegerField()
    total_marks = models.IntegerField()
    result = models.CharField(max_length=4)
    percentage = models.FloatField()
```

## Views

- **home_views**: Displays all students and handles filtering by name and result.
- **add_views**: Handles adding new student records.
- **delete_views**: Deletes a student record.
- **edit_views**: Edits an existing student record.
- **view**: Displays detailed information about a specific student.
- **about**: Displays information about the project.

