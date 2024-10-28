from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [

    path('', views.home, name='Home'),
    path('home/' , views.home , name = 'home'),
    path('about/', views.about, name='about'),
    path('services/' , views.services , name = 'services'),
    path('aftersub/' , views.aftersub , name = 'formsubmitted')
]
