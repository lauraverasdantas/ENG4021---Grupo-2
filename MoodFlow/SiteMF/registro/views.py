from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def registro(request):
    """
    Cadastro de novo usuário.

    GET  -> mostra o formulário.
    POST -> valida os dados, cria o User (senha com hash via create_user),
            autentica e redireciona para a home.

    Observação: os campos 'data_nasc' e 'telefone' do formulário NÃO são
    armazenados ainda, pois o User padrão do Django não os possui. Eles exigem
    um model de Perfil separado (tarefa futura).
    """
    if request.method != "POST":
        return render(request, "registro/registro.html")

    nome = (request.POST.get("nome") or "").strip()
    email = (request.POST.get("email") or "").strip()
    usuario = (request.POST.get("usuario") or "").strip()
    senha = request.POST.get("senha") or ""

    # Validações básicas
    if not usuario or not senha or not email:
        messages.error(request, "Preencha usuário, e-mail e senha.")
        return render(request, "registro/registro.html")

    if User.objects.filter(username=usuario).exists():
        messages.error(request, "Esse nome de usuário já está em uso.")
        return render(request, "registro/registro.html")

    if User.objects.filter(email=email).exists():
        messages.error(request, "Já existe uma conta com esse e-mail.")
        return render(request, "registro/registro.html")

    # Cria o usuário (create_user já aplica hash na senha)
    user = User.objects.create_user(username=usuario, email=email, password=senha)

    # Mapeia o nome completo para first_name / last_name
    partes = nome.split(" ", 1)
    user.first_name = partes[0]
    if len(partes) > 1:
        user.last_name = partes[1]
    user.save()

    # Já loga o usuário recém-criado e leva para a home
    auth_login(request, user)
    messages.success(request, "Conta criada com sucesso!")
    return redirect("home")
