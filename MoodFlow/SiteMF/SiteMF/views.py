from datetime import date
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.dateparse import parse_date
from SiteMF.models import PerfilUsuario, RegistroHumor
from SiteMF.models import ContatoConfianca
import json
import calendar


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = False

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse("painel_superuser")

        redirect_to = self.get_redirect_url()
        if redirect_to:
            return redirect_to

        return reverse("pos_login")


def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'SiteMF/home.html')


def sobre(request):
    return render(request, 'sobre.html')
    

def registro(request):
    """
    Cadastro de novo usuário.

    GET  -> mostra o formulário.
    POST -> valida os dados, cria o User (senha com hash via create_user),
            autentica e redireciona para a home.

    Os campos do formulário são salvos no User padrão e em um perfil
    relacionado com data de nascimento e telefone.
    """
    if request.method != "POST":
        return render(request, "SiteMF/registro.html")

    nome = (request.POST.get("nome") or "").strip()
    data_nasc = parse_date(request.POST.get("data_nasc") or "")
    telefone = (request.POST.get("telefone") or "").strip()
    email = (request.POST.get("email") or "").strip()
    usuario = (request.POST.get("usuario") or "").strip()
    senha = request.POST.get("senha") or ""

    # Validações básicas
    if not usuario or not senha or not email or not nome or not data_nasc or not telefone:
        messages.error(request, "Preencha nome, data de nascimento, telefone, usuário, e-mail e senha.")
        return render(request, "SiteMF/registro.html")

    if User.objects.filter(username=usuario).exists():
        messages.error(request, "Esse nome de usuário já está em uso.")
        return render(request, "SiteMF/registro.html")

    if User.objects.filter(email=email).exists():
        messages.error(request, "Já existe uma conta com esse e-mail.")
        return render(request, "SiteMF/registro.html")

    # Cria o usuário (create_user já aplica hash na senha)
    user = User.objects.create_user(username=usuario, email=email, password=senha)

    # Mapeia o nome completo para first_name / last_name
    partes = nome.split(" ", 1)
    user.first_name = partes[0]
    if len(partes) > 1:
        user.last_name = partes[1]
    user.save()

    PerfilUsuario.objects.create(
        usuario=user,
        data_nasc=data_nasc,
        telefone=telefone,
    )

    # Já loga o usuário recém-criado e leva para a home
    auth_login(request, user)
    messages.success(request, "Conta criada com sucesso!")
    return redirect("home")


# Mapeamento emoji → cor de fundo do card (mesmas cores do humor.html)
COR_EMOJI = {
    1: '#9288e0',  # Normal     — roxo
    2: '#5da7dd',  # Triste     — azul
    3: '#fbce3b',  # Feliz      — amarelo
    4: '#56c15b',  # Esperançoso— verde
    5: '#ed6e5f',  # Raivoso    — vermelho
    6: '#f18ca4',  # Apaixonado — rosa
    7: '#7c8d9e',  # Preocupado — cinza
    8: '#e78c46',  # Ansioso    — laranja
    9: '#cf724b',  # Entediado  — marrom
}

EMOJI_CHAR = {
    1: '😐', 2: '😢', 3: '😄', 4: '🌱',
    5: '😠', 6: '😍', 7: '😟', 8: '😰', 9: '😑',
}

MESES_PT = [
    '', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',
]


@login_required
def calendario(request):
    hoje = date.today()

    # Ano e mês vêm da query string (?ano=2026&mes=6) ou padrão = mês atual
    try:
        ano = int(request.GET.get('ano', hoje.year))
        mes = int(request.GET.get('mes', hoje.month))
        if not (1 <= mes <= 12):
            mes = hoje.month
        if not (2000 <= ano <= 2100):
            ano = hoje.year
    except (ValueError, TypeError):
        ano, mes = hoje.year, hoje.month

    # Navegação: mês anterior e próximo
    if mes == 1:
        mes_anterior, ano_anterior = 12, ano - 1
    else:
        mes_anterior, ano_anterior = mes - 1, ano

    if mes == 12:
        mes_proximo, ano_proximo = 1, ano + 1
    else:
        mes_proximo, ano_proximo = mes + 1, ano

    dias_no_mes = calendar.monthrange(ano, mes)[1]

    # Busca registros do usuário no mês/ano selecionado
    registros = (
        RegistroHumor.objects
        .filter(
            usuario=request.user,
            data_hora__year=ano,
            data_hora__month=mes,
        )
        .order_by('data_hora')
    )

    # Agrupa por dia: pega o ÚLTIMO registro do dia (mais recente)
    dados_por_dia = {}
    for r in registros:
        dia = r.data_hora.day
        dados_por_dia[dia] = {
            'emoji_num':   r.humor_emoji,
            'emoji_char':  EMOJI_CHAR.get(r.humor_emoji, ''),
            'emoji_label': r.get_humor_emoji_display(),
            'ansiedade':   r.nivel_ansiedade,
            'cor':         COR_EMOJI.get(r.humor_emoji, '#72A5D3'),
            'hora':        r.data_hora.strftime('%H:%M'),
        }

    context = {
        'ano':           ano,
        'mes':           mes,
        'mes_nome':      MESES_PT[mes],
        'dias_no_mes':   dias_no_mes,
        'mes_anterior':  mes_anterior,
        'ano_anterior':  ano_anterior,
        'mes_proximo':   mes_proximo,
        'ano_proximo':   ano_proximo,
        'hoje_dia':      hoje.day if (hoje.year == ano and hoje.month == mes) else None,
        'dados_por_dia': dados_por_dia,
        'total_registros': len(dados_por_dia),
    }
    return render(request, 'SiteMF/calendario.html', context)


@login_required
def humor(request):
    # Busca o contato de confiança do usuário logado (pode ser None)
    contato = (
        ContatoConfianca.objects
        .filter(usuario=request.user)
        .first()
    )

    if request.method == "POST":
        humor_emoji = request.POST.get("humor_emoji")
        nivel_ansiedade = request.POST.get("nivel_ansiedade")
        texto_livre = (request.POST.get("texto_livre") or "").strip()

        if not humor_emoji or not nivel_ansiedade:
            messages.error(request, "Selecione um humor e informe o nível de ansiedade.")
            return render(request, 'SiteMF/humor.html', {'contato': contato})

        try:
            humor_emoji = int(humor_emoji)
            nivel_ansiedade = int(nivel_ansiedade)
        except ValueError:
            messages.error(request, "Os dados do humor precisam ser numéricos.")
            return render(request, 'SiteMF/humor.html', {'contato': contato})

        RegistroHumor.objects.create(
            usuario=request.user,
            humor_emoji=humor_emoji,
            nivel_ansiedade=nivel_ansiedade,
            texto_livre=texto_livre,
        )
        messages.success(request, "Humor registrado com sucesso!")
        return redirect('calendario')

    return render(request, 'SiteMF/humor.html', {'contato': contato})


@login_required
def crise(request):
    return render(request, 'SiteMF/crise.html')


def _garantir_usuarios_demo():
    usuarios_reais = User.objects.filter(is_superuser=False)
    if usuarios_reais.exists():
        return

    demos = [
        {
            "username": "maria_demo",
            "email": "maria.demo@moodflow.local",
            "first_name": "Maria",
            "last_name": "Silva",
            "telefone": "(11) 99999-9999",
            "data_nasc": date(1995, 4, 15),
        },
        {
            "username": "joao_demo",
            "email": "joao.demo@moodflow.local",
            "first_name": "João",
            "last_name": "Souza",
            "telefone": "(21) 98888-7777",
            "data_nasc": date(1998, 8, 22),
        },
        {
            "username": "ana_demo",
            "email": "ana.demo@moodflow.local",
            "first_name": "Ana",
            "last_name": "Mendes",
            "telefone": "(31) 97777-6666",
            "data_nasc": date(2001, 11, 5),
        },
    ]

    for demo in demos:
        user, created = User.objects.get_or_create(
            username=demo["username"],
            defaults={
                "email": demo["email"],
                "first_name": demo["first_name"],
                "last_name": demo["last_name"],
            },
        )
        if created:
            user.set_password("Demo@12345")
            user.save()

        PerfilUsuario.objects.get_or_create(
            usuario=user,
            defaults={
                "telefone": demo["telefone"],
                "data_nasc": demo["data_nasc"],
            },
        )


@login_required
def removerusuario(request):
    if not request.user.is_superuser:
        return redirect('home')

    _garantir_usuarios_demo()

    if request.method == "POST":
        user_id = request.POST.get("user_id")
        if user_id:
            try:
                usuario = User.objects.get(id=user_id, is_superuser=False)
                nome_exibicao = usuario.get_full_name().strip() or usuario.username
                usuario.delete()
                messages.success(request, f"Usuário {nome_exibicao} removido com sucesso.")
            except User.DoesNotExist:
                messages.error(request, "Usuário não encontrado para remoção.")
        return redirect('removerusuario')

    usuarios = (
        User.objects
        .filter(is_superuser=False)
        .select_related('perfil')
        .order_by('first_name', 'username')
    )

    return render(request, 'SiteMF/removerusuario.html', {'usuarios': usuarios})


@login_required
def listarusuario(request):
    if not request.user.is_superuser:
        return redirect('home')

    _garantir_usuarios_demo()
    usuarios = (
        User.objects
        .filter(is_superuser=False)
        .select_related('perfil')
        .order_by('first_name', 'username')
    )

    return render(request, 'SiteMF/listarusuario.html', {'usuarios': usuarios})


@login_required
def editarperfil(request):
    return render(request, 'SiteMF/editarperfil.html')


@login_required
def painel_superuser(request):
    if not request.user.is_superuser:
        return redirect('home')

    return render(request, 'SiteMF/painel_superuser.html')


def sobre(request):
    return render(request, 'SiteMF/sobre.html')



@login_required
def contatoconfianca(request):
    """
    GET  → exibe o formulário de cadastro de contato de confiança.
    POST → valida e salva o contato no banco, depois redireciona para o humor.

    Aparece logo após o login (LOGIN_REDIRECT_URL aponta para cá).
    O usuário pode pular clicando em 'Fazer depois'.
    """
    # Carrega contato existente (se houver) para exibir na tela
    contato_existente = (
        ContatoConfianca.objects
        .filter(usuario=request.user)
        .first()
    )

    if request.method != 'POST':
        return render(request, 'SiteMF/contatoconfianca.html', {
            'contato': contato_existente,
            'opcoes_relacao': ContatoConfianca.Relacao.choices,
        })

    nome    = (request.POST.get('nome_contato') or '').strip()
    telefone = (request.POST.get('telefone') or '').strip()
    relacao  = (request.POST.get('relacao') or '').strip()

    if not nome or not telefone or not relacao:
        messages.error(request, 'Preencha todos os campos.')
        return render(request, 'SiteMF/contatoconfianca.html', {
            'contato': contato_existente,
            'opcoes_relacao': ContatoConfianca.Relacao.choices,
        })

    # Upsert: atualiza se já existe, cria se não existe
    ContatoConfianca.objects.update_or_create(
        usuario=request.user,
        defaults={
            'nome_contato': nome,
            'telefone':     telefone,
            'relacao':      relacao,
        },
    )

    messages.success(request, f'Contato "{nome}" salvo com sucesso!')
    return redirect('humor')


@login_required
def listarcontatosconfianca(request):
    contatos = (
        ContatoConfianca.objects
        .filter(usuario=request.user)
        .order_by('nome_contato')
    )

    return render(request, 'SiteMF/listarcontatosconfianca.html', {
        'contatos': contatos,
    })


@login_required
def pos_login(request):
    return render(request, 'SiteMF/pos_login.html')

def manual(request):
    return render(request, 'SiteMF/manual.html')
