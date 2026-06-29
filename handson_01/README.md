# Hands-On 1 – Django Project Setup and URL Routing

## Overview

This hands-on introduces the fundamentals of Django by creating a new project and application, configuring URL routing, and implementing basic views. It demonstrates the structure of a Django project and how HTTP requests are handled.

---

## Objectives

- Install and configure Django.
- Create a Django project and application.
- Understand Django project structure.
- Configure URL routing.
- Implement function-based views.
- Run and test the Django development server.

---

## Technologies Used

- Python 3.13
- Django 6.x
- SQLite3
- Visual Studio Code

---

## Project Structure

```
handson_01/
│
├── coursemanager/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── courses/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# Task 1 – Django Project Setup

## Description

Created a Django project named **coursemanager** and an application named **courses**.

### Activities Performed

- Installed Django
- Created a Django project
- Created a Django application
- Configured project settings
- Started the development server

---

# Task 2 – URL Routing

## Description

Configured URL routing between the project and application.

### Activities Performed

- Created application URLs
- Connected application URLs to project URLs
- Configured route mapping
- Verified URL navigation

---

# Task 3 – Function-Based Views

## Description

Implemented simple function-based views to return HTTP responses.

### Features Implemented

- Home page view
- About page view
- Course page view

---

## Testing

Verified the application by running the Django development server and accessing all configured URLs in the browser.

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
cd PythonBackendFrameworks/kalvimathi/handson_01
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

Run the server

```bash
python manage.py runserver
```

---

## Learning Outcomes

After completing this hands-on, the following concepts were understood:

- Django project architecture
- Django applications
- URL routing
- Function-based views
- Django development server

---

## Author

**Kalvimathi**

Python Backend Frameworks – Hands-On 1