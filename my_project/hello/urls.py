from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("day", views.current_day),
    path("quote", views.quote_day)
]