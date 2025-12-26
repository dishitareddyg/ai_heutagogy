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