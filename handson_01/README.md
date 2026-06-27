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
```

---

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

```bash
python manage.py migrate
```

This command creates the default Django database tables.

---

## Running the Application

```bash
python manage.py runserver
```

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

---

# Project Structure

```text
handson_01/
│
├── README.md
├── notes.py
├── requirements.txt
├── manage.py
│
├── coursemanager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── courses/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── migrations/
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
