"""BD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .views import inicio,InicioSesion,metaspagina,login,logout,register,registro,registrar,meta,perfil

urlpatterns = [
    path('', inicio,name='inicio'),
    path('inicio.html', inicio,name='inicio'),
    path('InicioSesion.html', login,name='InicioSesion'),
    path('Registro.html', registro,name='registro'),
    path('register', register,name='register'),
    path('Metas.html', metaspagina,name='metas'),
    path('inicioSesion.html', logout ,name='cerrar'),
    path('registrar', registrar, name='registro2'),
    path('metas', meta, name='metasg'),
    path('perfil', perfil, name='perfil')
    

    
    
    
]




