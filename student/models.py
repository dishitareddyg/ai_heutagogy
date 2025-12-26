
from django.db import models
from django.contrib.auth.models import User

class Roadmap(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    learner_profile = models.JSONField()
    roadmap_json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

