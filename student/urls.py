

app_name = "student"  
from django.urls import path
#from .views import module1
from .views import module1_view,module1_assessment_view
urlpatterns = [
    #path("create/", topic_input, name="topic_input"),
    path("module1/", module1_view, name="module1"),
    path("module1/assessment/", module1_assessment_view, name="module1_assessment"),
    
]
