# Hands-On 1: Web Framework Foundations & Django Project Setup

## Objective

Understand Django web framework fundamentals, the request-response lifecycle, middleware, WSGI vs ASGI, MVC/MVT architecture, and create a basic Django project with a working endpoint.

---

## Topics Covered

- Web Framework Concepts
- Request-Response Cycle
- MVC / MVT Pattern
- WSGI vs ASGI
- Django Project Setup
- URL Routing
- Middleware

---

## Project Setup

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

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

### Create Django App

```bash
python manage.py startapp courses
```

---

## Request-Response Lifecycle

A GET request to `/api/hello/` follows this path:

```text
Browser
   ↓
URL Router (urls.py)
   ↓
View (views.py)
   ↓
Model (Database Query if required)
   ↓
HttpResponse
   ↓
Browser
```

---

## Middleware Examples

### SecurityMiddleware

Provides security enhancements such as:

- HTTPS redirection
- Security headers
- Protection against common attacks

### SessionMiddleware

Provides:

- Session management
- Cookie handling
- User session tracking

---

## WSGI vs ASGI

### WSGI

- Synchronous interface
- Traditional Django deployment
- Suitable for standard web applications

### ASGI

- Asynchronous interface
- Supports WebSockets
- Supports real-time applications
- Suitable for chat and live notification systems

---

## MVC to Django MVT Mapping

| MVC | Django MVT |
|------|-----------|
| Model | Model |
| View | Template |
| Controller | View |

### Django MVT

- Model → Database layer
- View → Business logic
- Template → Presentation layer

---

## Application Endpoint

### View

```python
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Course Management API is running")
```

### URL Configuration

```python
urlpatterns = [
    path('api/', include('courses.urls')),
]
```

### Endpoint

```text
http://127.0.0.1:8000/api/hello/
```

### Expected Output

```text
Course Management API is running
```

---

## Run Migrations

```bash
python manage.py migrate
```

---

## Start Development Server

```bash
python manage.py runserver
```

---

## Folder Structure

```text
handson_01/
│
├── manage.py
├── requirements.txt
├── README.md
├── notes.py
│
├── coursemanager/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── courses/
    ├── views.py
    ├── urls.py
    └── ...
```

---

## Expected Outcome

- Django project created successfully
- Django app registered in INSTALLED_APPS
- URL routing configured
- Working endpoint available at `/api/hello/`
- Understanding of request-response lifecycle, middleware, WSGI/ASGI, and MVC/MVT architecture

---

## Requirements

```text
Django
```

Generate requirements file:

```bash
pip freeze > requirements.txt
```