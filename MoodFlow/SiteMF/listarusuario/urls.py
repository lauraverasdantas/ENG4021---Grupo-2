from django.urls import path
from . import views

app_name = 'listarusuario'

urlpatterns = [
    path("", views.listarusuario, name="listarusuario"),
    path("listarusuario/", views.listarusuario),
]
