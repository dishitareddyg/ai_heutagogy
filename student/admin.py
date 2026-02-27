from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Topic, StudentProgress

admin.site.register(Topic)
admin.site.register(StudentProgress)
