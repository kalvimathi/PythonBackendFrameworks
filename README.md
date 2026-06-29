# Python Backend Frameworks

## Overview

This repository contains my hands-on exercises completed as part of the **Python Backend Frameworks** course. The exercises focus on learning backend web development using Python frameworks, beginning with Django and gradually progressing toward building RESTful APIs.

Each hands-on demonstrates a specific concept and builds upon the previous one, providing practical experience in backend development.

---

## Technologies Used

- Python 3.13
- Django 6.x
- Django REST Framework (DRF)
- SQLite3
- Visual Studio Code
- Git & GitHub
- Insomnia (API Testing)

---

## Repository Structure

```
PythonBackendFrameworks/
│
├── handson_01/
│   ├── README.md
│   ├── manage.py
│   ├── requirements.txt
│   ├── coursemanager/
│   └── courses/
│
├── handson_02/
│   ├── README.md
│   ├── manage.py
│   ├── requirements.txt
│   ├── coursemanager/
│   └── courses/
│
├── handson_03/
│   ├── README.md
│   ├── manage.py
│   ├── requirements.txt
│   ├── coursemanager/
│   └── courses/
│
└── README.md
```

---

# Hands-On Summary

## Hands-On 1 – Django Project Setup and URL Routing

### Objective

Learn the fundamentals of Django by creating a project, configuring applications, implementing URL routing, and creating basic views.

### Topics Covered

- Installing Django
- Creating a Django Project
- Creating a Django Application
- URL Routing
- Function-Based Views
- Running the Development Server

### Skills Learned

- Django project structure
- URL configuration
- Basic request handling
- Django development workflow

---

## Hands-On 2 – Django Models and ORM

### Objective

Learn how to design database models and interact with the database using Django's Object Relational Mapper (ORM).

### Topics Covered

- Creating Models
- ForeignKey Relationships
- Database Migrations
- CRUD Operations
- Django Shell
- Querying Related Models

### Models Created

- Department
- Course
- Student
- Enrollment

### Skills Learned

- Database design
- Model relationships
- Django ORM
- CRUD operations
- Query optimization

---

## Hands-On 3 – Django REST Framework

### Objective

Develop RESTful APIs using Django REST Framework by implementing serializers, APIViews, ViewSets, and Routers.

### Topics Covered

### Task 1

- Django REST Framework Setup
- ModelSerializer
- APIView
- CRUD APIs
- URL Routing

### Task 2

- ModelViewSet
- DefaultRouter
- Automatic CRUD Endpoints
- API Testing using Insomnia

### Skills Learned

- REST API development
- API serialization
- CRUD API implementation
- ViewSets
- Routers
- API testing

---

## Packages Used

```
Django
djangorestframework
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kalvimathi/PythonBackendFrameworks.git
```

### 2. Navigate to the Repository

```bash
cd PythonBackendFrameworks
```

### 3. Open the Required Hands-On

Example:

```bash
cd handson_03
```

### 4. Create a Virtual Environment

```bash
python -m venv venv
```

### 5. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 6. Install Dependencies

```bash
pip install -r requirements.txt
```

### 7. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

---

## Learning Outcomes

By completing these hands-on exercises, I gained practical experience in:

- Django project development
- URL routing
- Function-based views
- Database modeling
- Django ORM
- Model relationships
- Database migrations
- REST API development
- Django REST Framework
- API serialization
- CRUD operations
- ViewSets and Routers
- API testing using Insomnia
- Git and GitHub version control



---

## Author

**Kalvimathi**

Python Backend Frameworks 