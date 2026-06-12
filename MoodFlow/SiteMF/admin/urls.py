Python
from django.urls import path
from . import views

urlpatterns = [
    # ... suas rotas existentes (home, crise, etc.)
    path('listarusuario/', views.listarusuario, name='listarusuario'),
    path('admin-custom/excluir/<int:user_id>/', views.excluir_usuario, name='excluir_usuario'),
]