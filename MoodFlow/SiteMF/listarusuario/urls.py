from django.urls import path
from . import views

app_name = 'listarusuario'

urlpatterns = [

    path('listarusuario/', views.listarusuario, name='listarusuario'),
]