from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm, UserUpdateForm
from .models import Profile


@login_required
def editar_perfil(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Perfil atualizado com sucesso.")
            return redirect("editarperfil:editar_perfil")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "profile": profile,
    }
    return render(request, "editarperfil/editarperfil.html", context)
