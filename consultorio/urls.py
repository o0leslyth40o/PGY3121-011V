from django.urls import path, include
from .import views


URLPatterns=[
    path('', views.index, name="index"),
]