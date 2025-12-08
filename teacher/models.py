from django.db import models

# Create your models here.
'''from django.db import models
from django.contrib.auth.models import User

class TeacherCourse(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    outcomes = models.TextField()
    num_classes = models.IntegerField()
    class_duration = models.IntegerField()
    class_size = models.IntegerField()
    roadmap = models.TextField(blank=True, null=True)
    '''

from django.db import models


class CoursePlan(models.Model):
    course_name = models.CharField(max_length=200)
    course_outcomes = models.TextField()
    num_classes = models.IntegerField()
    class_duration = models.IntegerField()   # minutes
    class_size = models.IntegerField()
    roadmap = models.TextField()             # generated roadmap JSON or text
    created_at = models.DateTimeField(auto_now_add=True)

class StudentProgress(models.Model):
    student_name = models.CharField(max_length=100)
    activity = models.CharField(max_length=200)
    progress_percent = models.IntegerField()
