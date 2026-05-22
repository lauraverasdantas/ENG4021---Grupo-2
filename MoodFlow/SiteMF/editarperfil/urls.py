from django.urls import path
from . import views

app_name = 'editarperfil'

urlpatterns = [
    path("", views.editar_perfil, name="editar_perfil"),
    path("editar-perfil/", views.editar_perfil),
]
