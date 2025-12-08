from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class StudentLearning(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    outcomes = models.TextField()
    roadmap = models.TextField(blank=True, null=True)
    progress = models.IntegerField(default=0)
