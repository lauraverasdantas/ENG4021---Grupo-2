import calendar
import json
from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from humor.models import RegistroHumor


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
        'dados_json':    json.dumps(dados_por_dia),
        'total_registros': len(dados_por_dia),
    }
    return render(request, 'calendario/calendario.html', context)
