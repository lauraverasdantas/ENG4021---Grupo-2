from django.urls import path
from . import views

app_name = 'crise'

urlpatterns = [

    path('crise/', views.crise, name='crise'),
]