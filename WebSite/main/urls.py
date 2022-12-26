from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('Kinematika', views.Kinematika, name='Kinematika'),
    path('about', views.about, name='aboutpage'),
    path('DS_page', views.dynamik_static, name='DS_page'),
    path('HM_page', views.horizontal_mov, name='HM_page'),
]