"""
REQUEST-RESPONSE CYCLE

GET /api/courses/

Browser
  ↓
URL Router
  ↓
View
  ↓
Model (Database Query)
  ↓
Response

Middleware Examples

1. SecurityMiddleware
   Adds security headers and protections.

2. SessionMiddleware
   Handles user sessions and cookies.

WSGI vs ASGI

WSGI:
- Synchronous
- Traditional web apps

ASGI:
- Asynchronous
- Supports WebSockets
- Supports real-time applications

MVC to Django MVT

MVC Model      -> Django Model
MVC View       -> Django Template
MVC Controller -> Django View

MVT:
Model = Data
View = Logic
Template = UI
"""