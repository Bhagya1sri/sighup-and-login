from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sighup/',views.sighup,name='sighup'),
    path('login/',views.login,name='login'),
]
