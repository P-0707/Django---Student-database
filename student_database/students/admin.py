from django.contrib import admin
from . models import *

@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'email_id']

@admin.register(Dept)
class deptAdmin(admin.ModelAdmin):
    list_display = ['dept_name']

@admin.register(Course)
class courseAdmin(admin.ModelAdmin):
    list_display = ["course_id", "course_name", "instructor_id"]

@admin.register(Instructor)
class instructorAdmin(admin.ModelAdmin):
    list_display = ["instructor_id", "instructor_name", "instructor_email", "instructor_dept"]


