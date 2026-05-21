from django.urls import path
from . import views

app_name = 'removerusuario'

urlpatterns = [

    path('removerusuario/', views.removerusuario, name='removerusuario'),
]