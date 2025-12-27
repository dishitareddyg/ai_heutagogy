

app_name = "student"  
from django.urls import path
#from .views import module1
from .views import module1_view,module1_assessment_view,module1_resources_view
from . import views
from .views import os_graph



urlpatterns = [
   
    path("module1/", module1_view, name="module1"),
    path("module1/assessment/", module1_assessment_view, name="module1_assessment"),
    path("module1/resources/", module1_resources_view, name="module1_resources"),
    path("reflection/", views.reflection_view, name="reflection"),
    path("os/", os_graph, name="os_graph"),
]
