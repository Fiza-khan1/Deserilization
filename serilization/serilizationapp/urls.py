from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.getStudent ,name='Student'),
    path('createstudent/',views.createStudent ,name='createStudent'),
]