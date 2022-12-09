from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('Kinematika', views.Kinematika, name='Kinematika'),
    path('about', views.about, name='aboutpage'),
]