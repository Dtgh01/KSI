from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('myweb/', include('myweb.urls')),
    path('', views.index),
    path('about/', views.about),
]
