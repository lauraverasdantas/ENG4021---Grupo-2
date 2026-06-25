from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import date
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from contatoconfianca.models import ContatoConfianca
from SiteMF.models import RegistroHumor
import calendar
import json


def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'SiteMF/home.html')

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


#@login_required
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
        'dados_json':    json.dumps(dados_por_dia),
        'total_registros': len(dados_por_dia),
    }
    return render(request, 'SiteMF/calendario.html', context)

@login_required
def crise(request):
    return render(request, 'SiteMF/crise.html')

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
        return render(request, "SiteMF/registro.html")

    nome = (request.POST.get("nome") or "").strip()
    email = (request.POST.get("email") or "").strip()
    usuario = (request.POST.get("usuario") or "").strip()
    senha = request.POST.get("senha") or ""

    # Validações básicas
    if not usuario or not senha or not email:
        messages.error(request, "Preencha usuário, e-mail e senha.")
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

    # Já loga o usuário recém-criado e leva para a home
    auth_login(request, user)
    messages.success(request, "Conta criada com sucesso!")
    return redirect("home")

@login_required
def humor(request):
    # Busca o contato de confiança do usuário logado (pode ser None)
    contato = (
        ContatoConfianca.objects
        .filter(usuario=request.user)
        .first()
    )
    return render(request, 'SiteMF/humor.html', {'contato': contato})
