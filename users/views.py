from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegisgerForm
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.
class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisgerForm
    success_url = '/'

class LoginView(LoginView):
    template_name = 'users/login.html'

class LogoutView(LogoutView):
    template_name = 'users/login.html'



