

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
    path("one-minute-paper/", views.one_minute_paper, name="one_minute_paper"),
    path("story-map/", views.story_map_page, name="story_map"),
    path("story-map-feedback/", views.story_map_feedback, name="story_map_feedback"),
    path("learning-video/", views.learning_video, name="learning_video"),
    path('progress/', views.student_progress, name='progress'),
    path('complete/<int:topic_id>/', views.mark_topic_completed, name='mark_completed'),
    path("muddiest-point/",views.muddiest_point_view,name="muddiest_point"),
    path("assessment/", views.assessment, name="assessment"),
    path("assessment/submit/", views.submit_assessment, name="submit_assessment"),
    path("media/", views.media_library, name="media_library"),

    
]
