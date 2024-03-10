from django.contrib import admin
from django.urls import path
from e_app import views

urlpatterns = [
    path('',views.home)
    ]
