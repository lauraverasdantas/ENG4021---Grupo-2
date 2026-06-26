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
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Rotas corrigidas e individualizadas:
    path('calendario/', views.calendario, name='calendario'),
    path('crise/', views.crise, name='crise'),
    path('registro/', views.registro, name='registro'),
    path('humor/', views.humor, name='humor'),
    path('painel_superuser/', views.painel_superuser, name='painel_superuser'),
    path('removerusuario/', views.removerusuario, name='removerusuario'),
    path('listarusuario/', views.listarusuario, name='listarusuario'),
    path('editarperfil/', views.editarperfil, name='editarperfil'),
    path('sobre/', views.sobre, name='sobre'),
    path('contatoconfianca/', views.contatoconfianca, name='contatoconfianca'),
    path('listarcontatosconfianca/', views.listarcontatosconfianca, name='listarcontatosconfianca'),
    path('pos_login/', views.pos_login, name='pos_login'),
    path('contato/', views.contato, name='contato'),
]
