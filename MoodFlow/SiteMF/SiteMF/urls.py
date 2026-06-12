"""
URL configuration for SiteMF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from SiteMF import views
from django.urls import include
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('login/', include('login.urls')),
    path('registro/', include('registro.urls')),
    path('editarperfil/', include('editarperfil.urls')),
    path('listarusuario/', include('listarusuario.urls')),
    path('removerusuario/', include('removerusuario.urls')),
    path('humor/', include('humor.urls')),
    path('calendario/', include('calendario.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('crise/', include('crise.urls')),
    path('admin/', include('admin.urls')),
]
