from django.shortcuts import render
'''
# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User

def student_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password,
            role='student'
        )
        login(request, user)
        return redirect('student-dashboard')

    return render(request, 'accounts/student_signup.html')

# accounts/views.py
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.role == 'student':
            return '/student/dashboard/'
        elif user.role == 'teacher':
            return '/teacher/dashboard/'
        return '/'
'''

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("accounts:dashboard")

        messages.error(request, "Invalid credentials")

    return render(request, "accounts/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully")
            return redirect("accounts:login")

    return render(request, "accounts/signup.html")


def logout_view(request):
    logout(request)
    return redirect("accounts:login")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url="accounts:login")
def dashboard(request):
    return render(request, "accounts/dashboard.html")
