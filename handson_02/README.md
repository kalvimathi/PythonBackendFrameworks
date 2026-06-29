# Hands-On 2 – Django Models, ORM and Database Operations

## Overview

This hands-on demonstrates how to design database models using Django ORM, perform database migrations, create relationships between models, and execute CRUD operations using the Django Shell.

---

## Objectives

- Design relational database models.
- Implement model relationships using ForeignKey.
- Perform database migrations.
- Execute CRUD operations using Django ORM.
- Query related objects efficiently.

---

## Technologies Used

- Python 3.13
- Django 6.x
- SQLite3
- Django ORM

---

## Project Structure

```
handson_02/
│
├── coursemanager/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── courses/
│   ├── models.py
│   ├── migrations/
│   ├── views.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# Task 1 – Database Models

## Description

Created relational models representing a university course management system.

### Models Implemented

- Department
- Course
- Student
- Enrollment

### Relationships

- Department → Course (One-to-Many)
- Department → Student (One-to-Many)
- Student → Enrollment (One-to-Many)
- Course → Enrollment (One-to-Many)

---

# Task 2 – Database Migration

## Description

Generated and applied database migrations using Django migration commands.

### Commands Used

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Task 3 – Django ORM Operations

## Description

Performed CRUD operations using Django Shell.

### Operations Performed

- Created Departments
- Added Students
- Added Courses
- Created Enrollments
- Retrieved data
- Updated records
- Deleted records
- Queried related objects using `select_related()`
- Used `values()` for optimized queries

---

## Testing

Verified all database operations through the Django Shell.

---

## Packages Used

```
Django
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/kalvimathi/PythonBackendFrameworks.git
```

Navigate to the project

```bash
cd PythonBackendFrameworks/kalvimathi/handson_02
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create database

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the Django Shell

```bash
python manage.py shell
```

# output image 

![alt text](<Screenshot 2026-06-27 142701.png>) ![alt text](<Screenshot 2026-06-27 142721.png>) ![alt text](<Screenshot 2026-06-27 142730.png>)![alt text](<Screenshot 2026-06-27 191621.png>)![alt text](<Screenshot 2026-06-27 191635.png>) ![alt text](<Screenshot 2026-06-27 191643.png>) ![alt text](<Screenshot 2026-06-27 191656.png>) ![alt text](<Screenshot 2026-06-27 191704.png>) ![alt text](<Screenshot 2026-06-27 191710.png>)
---

## Learning Outcomes

After completing this hands-on, the following concepts were understood:

- Django ORM
- Database migrations
- Model relationships
- CRUD operations
- Query optimization using ORM
- Working with ForeignKey relationships

---

## Author

**Kalvimathi**

Python Backend Frameworks – Hands-On 2