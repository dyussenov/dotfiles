from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('about/', about, name='about'), 
    path('categories/<str:category>/', categories),
    path('contact/', contact),
    path('archive/<int:year>/', archive)
]