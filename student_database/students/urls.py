from students import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('student/<str:student_id>/', views.student, name="student"),
    path('course/<str:course_id>/', views.course_details, name='course_details'),
    path('instructor/<str:instructor_id>/', views.instructor, name='instructor'),
]