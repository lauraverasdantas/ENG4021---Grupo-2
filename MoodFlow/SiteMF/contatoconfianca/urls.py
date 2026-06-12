from django.urls import path
from . import views

app_name = 'contatoconfianca'

urlpatterns = [
    path('', views.cadastrar_contato, name='cadastrar_contato'),
]
