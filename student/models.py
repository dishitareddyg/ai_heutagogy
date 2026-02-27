
from django.db import models
from django.contrib.auth.models import User

class Roadmap(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    learner_profile = models.JSONField()
    roadmap_json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class StudentProgress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'topic')

    def __str__(self):
        return f"{self.student.username} - {self.topic.name}"

class AssessmentResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    assessment_type = models.CharField(max_length=50)
    score = models.IntegerField()
    total = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def percentage(self):
        return round((self.score / self.total) * 100, 2)

    def __str__(self):
        return f"{self.student.username} - {self.topic.name} - {self.score}/{self.total}"
