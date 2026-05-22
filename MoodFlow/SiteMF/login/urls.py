from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path("", views.login_view, name="login"),
    path("login/", views.login_view),
    path("sair/", views.logout_view, name="logout"),
]
