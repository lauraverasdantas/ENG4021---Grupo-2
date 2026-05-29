from django.urls import path
from . import views

app_name = 'humor'

urlpatterns = [

    path('humor/', views.humor, name='humor'),
]