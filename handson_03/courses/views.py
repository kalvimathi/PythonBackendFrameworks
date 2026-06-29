from rest_framework import viewsets

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on Course.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer