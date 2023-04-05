from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('categories/<str:category>/', categories) #127.0.0.1:8000/categories/cats
]