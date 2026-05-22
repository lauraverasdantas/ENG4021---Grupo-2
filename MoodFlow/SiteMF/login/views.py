from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import MoodFlowAuthenticationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = MoodFlowAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, "Login realizado com sucesso.")
            return redirect("home")
    else:
        form = MoodFlowAuthenticationForm(request)

    return render(request, "login/login.html", {"form": form})


@require_POST
def logout_view(request):
    auth_logout(request)
    messages.success(request, "Voce saiu da sua conta.")
    return redirect("home")
