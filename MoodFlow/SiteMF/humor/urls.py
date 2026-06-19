from django.urls import path
from . import views

app_name = 'humor'

urlpatterns = [
    path('humor/', views.humor, name='humor'),
  # path('historico/', views.historico, name='historico'),
   # path('estatisticas/', views.estatisticas, name='estatisticas'),
]
