from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('Kinematika', views.Knematika, name='Kinematika'),
]
