from django.contrib import admin
<<<<<<< HEAD
from .models import (
    Department,
    Course,
    Student,
    Enrollment
)

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Enrollment)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
        'credits',
        'department'
    )

    search_fields = (
        'name',
        'code'
    )

    list_filter = (
        'department',
    )
=======

# Register your models here.
>>>>>>> af693d4270880be1d980a0ae15e539d260fdb6e5
