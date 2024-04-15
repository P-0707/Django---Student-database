from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def student(request, student_id):
    print("Student ID:", student_id)
    try:
        student = Student.objects.get(student_id=student_id)
        return render(request, 'student.html', {'student': student})
    except Student.DoesNotExist:
        return HttpResponse("Student not found")  


def course_details(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    instructor = course.instructor_id
    return render(request, 'course.html', {'course': course, 'instructor': instructor})

def instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, instructor_id= instructor_id)
    return render(request, 'instructor.html', {'instructor':instructor})
