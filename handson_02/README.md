<<<<<<< HEAD
# Hands-On 2: Django Models, ORM Operations, and Admin Interface

## Overview

This hands-on exercise focuses on designing database models using Django ORM, performing database migrations, executing ORM queries, and configuring the Django Admin Interface for managing application data.

The project simulates a Course Management System containing departments, courses, students, and enrollments.

---

# Learning Objectives

By completing this exercise, the following concepts are demonstrated:

* Creating Django models and relationships
* Understanding database migrations
* Performing CRUD operations using Django ORM
* Working with QuerySets and advanced ORM features
* Using Aggregations and F Expressions
* Optimizing queries with `select_related()`
* Configuring and customizing Django Admin
* Managing application data through the Admin Interface

---

# Task 1: Database Design and Django Models

## Objective

Design and implement the database schema for a Course Management System.

---

## Models Created

### Department

Represents an academic department.

| Field        | Type         |
| ------------ | ------------ |
| name         | CharField    |
| head_of_dept | CharField    |
| budget       | DecimalField |

---

### Course

Represents a course offered by a department.

| Field      | Type                   |
| ---------- | ---------------------- |
| name       | CharField              |
| code       | CharField              |
| credits    | IntegerField           |
| department | ForeignKey(Department) |

Relationship:

```text
One Department → Many Courses
```

---

### Student

Represents a student enrolled in a department.

| Field           | Type                   |
| --------------- | ---------------------- |
| first_name      | CharField              |
| last_name       | CharField              |
| email           | EmailField             |
| enrollment_year | IntegerField           |
| department      | ForeignKey(Department) |

Relationship:

```text
One Department → Many Students
```

---

### Enrollment

Represents course enrollment information.

| Field           | Type                |
| --------------- | ------------------- |
| student         | ForeignKey(Student) |
| course          | ForeignKey(Course)  |
| enrollment_date | DateField           |
| grade           | CharField           |

Relationship:

```text
Many Students ↔ Many Courses
```

Implemented through the Enrollment model.

---

# Entity Relationship Overview

```text
Department
    │
    ├── Course
    │
    └── Student
            │
            └── Enrollment
                    │
                    └── Course
```

---

# Task 2: Database Migrations and ORM Operations

## Objective

Create database tables and perform ORM operations using Django's Object Relational Mapper.

---

## Generate Migrations

```bash
python manage.py makemigrations
=======
# Hands-On 1: Web Framework Foundations and Django Project Setup

## Overview

This hands-on exercise introduces the fundamental concepts of web frameworks and the Django framework. The objective is to understand the request-response lifecycle, middleware architecture, WSGI and ASGI interfaces, MVC/MVT design patterns, and create a basic Django application with a working API endpoint.

---

## Learning Objectives

By completing this hands-on exercise, the following concepts are demonstrated:

* Understanding the web request-response lifecycle
* Understanding the role of middleware in Django
* Comparing WSGI and ASGI application interfaces
* Understanding the MVC and Django MVT architectural patterns
* Setting up a Django project and application
* Configuring URL routing
* Creating and executing a basic Django view
* Running and testing a Django development server

---

# Task 1: Web Framework Fundamentals

## 1. Request-Response Cycle in Django

The request-response cycle describes how a client request is processed by a Django application.

### Flow

```text
Client (Browser/Postman)
        │
        ▼
URL Router (urls.py)
        │
        ▼
View Function/Class
        │
        ▼
Model Layer (Database Interaction)
        │
        ▼
Response Object
        │
        ▼
Client
```

### Explanation

1. The client sends an HTTP request.
2. Django URL dispatcher identifies the matching route.
3. The associated view function is executed.
4. The view may interact with models and the database.
5. A response is generated.
6. The response is returned to the client.

---

## 2. Middleware in Django

Middleware components process requests and responses globally across the application.

### SecurityMiddleware

Purpose:

* Provides security enhancements.
* Helps enforce HTTPS.
* Adds security-related HTTP headers.

Benefits:

* Protects against common web vulnerabilities.
* Improves application security.

### SessionMiddleware

Purpose:

* Manages user sessions.
* Stores and retrieves session data.
* Enables user authentication and tracking.

Benefits:

* Maintains user state between requests.
* Supports login sessions and personalized experiences.

---

## 3. WSGI vs ASGI

### WSGI (Web Server Gateway Interface)

Characteristics:

* Synchronous request handling.
* Suitable for traditional web applications.
* Widely supported by web servers.

Use Cases:

* Standard CRUD applications.
* Traditional Django deployments.

### ASGI (Asynchronous Server Gateway Interface)

Characteristics:

* Supports asynchronous programming.
* Handles WebSockets and long-lived connections.
* Enables real-time communication.

Use Cases:

* Chat applications.
* Live notifications.
* Real-time dashboards.
* Streaming services.

### Comparison

| Feature                       | WSGI        | ASGI         |
| ----------------------------- | ----------- | ------------ |
| Processing                    | Synchronous | Asynchronous |
| WebSockets                    | No          | Yes          |
| Real-Time Support             | Limited     | Excellent    |
| Performance Under Concurrency | Moderate    | High         |

---

## 4. MVC vs Django MVT Architecture

### Traditional MVC Pattern

| MVC Component | Responsibility         |
| ------------- | ---------------------- |
| Model         | Data Layer             |
| View          | User Interface         |
| Controller    | Request Handling Logic |

### Django MVT Pattern

| MVT Component | Responsibility             |
| ------------- | -------------------------- |
| Model         | Database and Business Data |
| View          | Application Logic          |
| Template      | User Interface             |

### MVC to MVT Mapping

| MVC        | Django MVT |
| ---------- | ---------- |
| Model      | Model      |
| View       | Template   |
| Controller | View       |

---

# Task 2: Django Project Setup

## Objective

Create a Django project named **coursemanager** and an application named **courses**. Configure URL routing and expose a simple API endpoint.

---

## Project Creation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Django

```bash
pip install django
```

### Create Django Project

```bash
django-admin startproject coursemanager .
```

### Create Django Application

```bash
python manage.py startapp courses
>>>>>>> af693d4270880be1d980a0ae15e539d260fdb6e5
```

---

<<<<<<< HEAD
## Apply Migrations
=======
## Application Configuration

### Register Application

The `courses` application was added to:

```python
INSTALLED_APPS
```

inside:

```python
coursemanager/settings.py
```

---

## Creating a Basic View

A simple view was implemented to verify application functionality.

### views.py

```python
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Course Management API is running")
```

---

## URL Configuration

### courses/urls.py

```python
from django.urls import path
from .views import hello_view

urlpatterns = [
    path('hello/', hello_view),
]
```

### project urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
]
```

---

## Database Migration
>>>>>>> af693d4270880be1d980a0ae15e539d260fdb6e5

```bash
python manage.py migrate
```

<<<<<<< HEAD
These commands generate and apply database schema changes.

---

## Sample Data Creation

Departments:

```python
cs = Department.objects.create(
    name="Computer Science",
    head_of_dept="Dr Smith",
    budget=100000
)

math = Department.objects.create(
    name="Mathematics",
    head_of_dept="Dr Brown",
    budget=80000
)
```

---

## ORM Query Examples

### Retrieve All Departments

```python
Department.objects.all()
```

---

### Filter Courses by Department

```python
Course.objects.filter(
    department__name="Computer Science"
)
```

Purpose:

* Returns all courses belonging to the Computer Science department.

---

### Aggregation Using Count

```python
from django.db.models import Count

Department.objects.values(
    'name'
).annotate(
    course_count=Count('course')
)
```

Purpose:

* Calculates the number of courses in each department.

---

### Query Optimization Using select_related()

```python
Student.objects.select_related(
    'department'
)
```

Purpose:

* Retrieves related department information in a single database query.
* Improves performance.

---

### F Expression Example

```python
from django.db.models import F

Department.objects.update(
    budget=F('budget') * 1.1
)
```

Purpose:

* Increases department budgets by 10%.
* Performs the calculation directly in the database.

---

# Task 3: Django Admin Interface

## Objective

Configure Django Admin to manage application data efficiently.

---

## Registered Models

The following models were registered:

* Department
* Course
* Student
* Enrollment

---

## Admin Customization

The Course model was customized using `ModelAdmin`.

### Features Implemented

#### List Display

```python
list_display = (
    'name',
    'code',
    'credits',
    'department'
)
```

Displays important course details in the admin list page.

---

#### Search Functionality

```python
search_fields = (
    'name',
    'code'
)
```

Allows searching courses by:

* Course Name
* Course Code

---

#### Filtering

```python
list_filter = (
    'department',
)
```

Allows filtering courses by department.

---

## Superuser Creation

```bash
python manage.py createsuperuser
```

Used to access the Django administration panel.

---

## Accessing Admin Dashboard

Start the development server:
=======
This command creates the default Django database tables.

---

## Running the Application
>>>>>>> af693d4270880be1d980a0ae15e539d260fdb6e5

```bash
python manage.py runserver
```

<<<<<<< HEAD
Open:

```text
http://127.0.0.1:8000/admin/
```

Login using superuser credentials.
=======
The development server starts at:

```text
http://127.0.0.1:8000/
```

---

## Testing the Endpoint

### Endpoint

```text
http://127.0.0.1:8000/api/hello/
```

### Expected Response

```text
Course Management API is running
```
>>>>>>> af693d4270880be1d980a0ae15e539d260fdb6e5

---

# Project Structure

```text
<<<<<<< HEAD
handson_02/
│
├── README.md
=======
handson_01/
│
├── README.md
├── notes.py
>>>>>>> af693d4270880be1d980a0ae15e539d260fdb6e5
├── requirements.txt
├── manage.py
│
├── coursemanager/
<<<<<<< HEAD
=======
│   ├── __init__.py
>>>>>>> af693d4270880be1d980a0ae15e539d260fdb6e5
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── courses/
<<<<<<< HEAD
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    ├── views.py
    └── __init__.py
=======
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── migrations/
>>>>>>> af693d4270880be1d980a0ae15e539d260fdb6e5
```

---

# Requirements

```text
Django
```

Generate requirements file:

```bash
pip freeze > requirements.txt
```

---

# Outcome

Successfully completed:

<<<<<<< HEAD
## Task 1

* Designed and implemented database models
* Created model relationships using Foreign Keys

## Task 2

* Generated and applied migrations
* Inserted sample data
* Performed filtering, aggregation, optimization, and update operations using ORM

## Task 3

* Registered models in Django Admin
* Customized Course administration interface
* Enabled search and filtering
* Created superuser and verified admin functionality

This exercise demonstrates practical usage of Django ORM and Admin Interface for managing relational data in a web application.
=======
✅ Task 1 – Web Framework Fundamentals

* Request-Response Cycle
* Middleware Concepts
* WSGI vs ASGI
* MVC vs Django MVT

✅ Task 2 – Django Project Setup

* Django Installation
* Project Creation
* Application Creation
* URL Routing Configuration
* Basic View Implementation
* Development Server Execution
* Endpoint Verification

This hands-on provides a foundational understanding of Django architecture and project setup, preparing for advanced topics such as Models, ORM, Admin Interface, and REST APIs in subsequent exercises.
>>>>>>> af693d4270880be1d980a0ae15e539d260fdb6e5
