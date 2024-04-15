from django.db import models

gender_choices = [
    ('M', 'Male'),
    ('F', 'Female')
]

class Dept(models.Model):
    dept_name = models.CharField(max_length = 40)

    
    def __str__(self):
        return self.dept_name

class Instructor(models.Model):
    instructor_id = models.CharField(max_length = 20, primary_key = True)
    instructor_name = models.CharField(max_length = 100)
    instructor_email = models.EmailField(max_length = 100, unique = True)
    instructor_dept = models.ForeignKey(Dept, on_delete = models.CASCADE)
    course_taught = models.ManyToManyField('Course', blank=True)

    def __str__(self):
        return self.instructor_id

class Course(models.Model):
    course_id = models.CharField(max_length = 20, unique = True, primary_key = True)
    course_name = models.CharField(max_length =100)
    course_description = models.TextField()
    instructor_id = models.ForeignKey(Instructor, on_delete = models.CASCADE)

class Student(models.Model):
    student_id = models.CharField(max_length = 20, unique = True, primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 20, blank = True)
    email_id = models.EmailField(max_length = 100, unique = True)
    phone_number = models.CharField(max_length = 10, unique = True)
    student_gender = models.CharField(choices = gender_choices, max_length = 1)
    student_address = models.TextField(max_length = 100)
    student_dept = models.ForeignKey('Dept', on_delete = models.CASCADE)
    date_of_birth = models.DateField()
    enrolled_courses = models.ManyToManyField(Course)










