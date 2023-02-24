from django.contrib import admin
from django.urls import path
from productmanager import views

urlpatterns = [
    path('',views.index),
    path('apple/',views.apple),
    path('sumsang/',views.sumsang),
    path('vivo/',views.vivo),
]