'''
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
'''
from django.urls import path
from .views import login_view, register_view, logout_view
from .import views
app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
