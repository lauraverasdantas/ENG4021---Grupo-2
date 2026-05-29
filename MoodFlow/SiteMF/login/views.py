from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render


def login(request):
    """
    Autenticação do usuário.

    GET  -> mostra o formulário de login.
    POST -> autentica com usuário/senha. Se válido, cria a sessão e vai para a
            home; senão, mostra mensagem de erro.
    """
    if request.method != "POST":
        return render(request, "login/login.html")

    usuario = (request.POST.get("usuario") or "").strip()
    senha = request.POST.get("senha") or ""

    user = authenticate(request, username=usuario, password=senha)
    if user is None:
        messages.error(request, "Usuário ou senha inválidos.")
        return render(request, "login/login.html")

    auth_login(request, user)
    return redirect("home")


def logout(request):
    """Encerra a sessão e volta para a tela de login."""
    auth_logout(request)
    messages.success(request, "Você saiu da sua conta.")
    return redirect("login:login")
