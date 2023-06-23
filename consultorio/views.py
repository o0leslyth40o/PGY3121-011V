from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Create your views here.
def index(request):
    return render(request, 'consultorio/index.html')