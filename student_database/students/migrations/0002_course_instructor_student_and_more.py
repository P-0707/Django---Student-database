# Generated by Django 4.2.11 on 2024-04-02 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='instructor',
            fields=[
                ('instructor_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('instructor_name', models.CharField(max_length=100)),
                ('instructor_email', models.EmailField(max_length=100, unique=True)),
                ('course_taught', models.ManyToManyField(to='students.course')),
                ('instructor_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.dept')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('student_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('email_id', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('student_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('student_address', models.TextField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('enrolled_courses', models.ManyToManyField(to='students.course')),
                ('student_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.dept')),
            ],
        ),
        migrations.RemoveField(
            model_name='students',
            name='student_dept',
        ),
        migrations.DeleteModel(
            name='branch',
        ),
        migrations.DeleteModel(
            name='students',
        ),
        migrations.AddField(
            model_name='course',
            name='instructor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.instructor'),
        ),
    ]