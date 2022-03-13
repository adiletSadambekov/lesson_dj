from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, DetailView
from django.utils import timezone
from .form import RegisterUsers
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.

def profile(request):
    return render(request, 'users/profile.html')




class RegisterUserView(CreateView):
    template_name = 'registration/register.html'
    success_url = '/acconts/login/'
    form_class = RegisterUsers


