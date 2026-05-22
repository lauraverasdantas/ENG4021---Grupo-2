from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render

from .forms import RegistrationForm


def registro(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Conta criada com sucesso.")
            return redirect("editarperfil:editar_perfil")
    else:
        form = RegistrationForm()

    return render(request, "registro/registro.html", {"form": form})
