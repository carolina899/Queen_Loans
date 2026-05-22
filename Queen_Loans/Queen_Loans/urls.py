"""
URL configuration for Queen_Loans project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Panel de administrador
    path('admin/', admin.site.urls),

    # Conectar las URLs de la app prestamos
    path('', include('prestamos.urls')),

]
