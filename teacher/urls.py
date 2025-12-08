
from django.urls import path
from . import views
#from .views import teacher_roadmap
urlpatterns = [
    
    #path("roadmap/", teacher_roadmap, name="teacher-roadmap"),
    path("plan/", views.create_plan, name="teacher-plan"),
    #path("roadmap/", views.teacher_roadmap, name="teacher-roadmap"),
    path("dashboard/", views.teacher_dashboard, name="teacher-dashboard"),
]
