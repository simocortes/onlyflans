"""onlyflans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web.views import index, about, welcome, message, exito, toggle_favorito, favoritos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('welcome/', welcome, name="welcome"),
    path('message/', message, name="message"),
    path('exito/', exito, name="exito"),
    path('accounts/', include('django.contrib.auth.urls')),  # Autenticación
    path('flan/<int:flan_id>/toggle-favorito/', toggle_favorito, name='toggle_favorito'),
    path('favoritos/', favoritos, name='favoritos'),
]



