from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [

    path('registro/', views.registro, name='registro'),
]