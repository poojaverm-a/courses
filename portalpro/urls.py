"""portalpro URL Configuration
"""
from django.contrib import admin
from django.urls import path,include
from protalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home',views.home),
    path('contact', views.contact),
    path('galary', views.galary),
    path('service', views.service),
]
