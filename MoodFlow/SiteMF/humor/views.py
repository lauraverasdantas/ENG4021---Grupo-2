from datetime import date, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.shortcuts import redirect, render

from contatoconfianca.models import ContatoConfianca

from .models import RegistroHumor


@login_required
def humor(request):
    # Ao enviar o formulário, salva um novo registro de humor.
    if request.method == 'POST':
        emoji = request.POST.get('humor_emoji')
        ansiedade = request.POST.get('nivel_ansiedade')
        texto = request.POST.get('texto_livre', '').strip()

        erros = []

        try:
            emoji = int(emoji)
            if not (1 <= emoji <= 9):
                erros.append('Selecione um humor válido.')
        except (TypeError, ValueError):
            erros.append('Selecione um humor antes de salvar.')

        try:
            ansiedade = int(ansiedade)
            if not (1 <= ansiedade <= 10):
                erros.append('O nível de ansiedade deve estar entre 1 e 10.')
        except (TypeError, ValueError):
            erros.append('Informe um nível de ansiedade válido.')

        if erros:
            for erro in erros:
                messages.error(request, erro)
        else:
            RegistroHumor.objects.create(
                usuario=request.user,
                humor_emoji=emoji,
                nivel_ansiedade=ansiedade,
                texto_livre=texto,
            )
            messages.success(request, 'Humor registrado com sucesso!')
            return redirect('calendario:calendario')

    contato = (
        ContatoConfianca.objects
        .filter(usuario=request.user)
        .first()
    )
    return render(request, 'humor/humor.html', {'contato': contato})


@login_required
def historico(request):
    """Lista os registros de humor do usuário, com filtro por data e emoji."""
    registros = RegistroHumor.objects.filter(usuario=request.user)

    data_inicio = request.GET.get('inicio', '').strip()
    data_fim = request.GET.get('fim', '').strip()
    emoji = request.GET.get('emoji', '').strip()

    if data_inicio:
        registros = registros.filter(data_hora__date__gte=data_inicio)
    if data_fim:
        registros = registros.filter(data_hora__date__lte=data_fim)
    if emoji:
        try:
            registros = registros.filter(humor_emoji=int(emoji))
        except ValueError:
            pass

    context = {
        'registros': registros,
        'opcoes_emoji': RegistroHumor.Emoji.choices,
        'inicio': data_inicio,
        'fim': data_fim,
        'emoji_selecionado': emoji,
        'total': registros.count(),
    }
    return render(request, 'humor/historico.html', context)


@login_required
def estatisticas(request):
    """Mostra estatísticas de humor do usuário nos últimos 30 dias."""
    inicio = date.today() - timedelta(days=30)
    registros = RegistroHumor.objects.filter(
        usuario=request.user,
        data_hora__date__gte=inicio,
    )

    total = registros.count()
    ansiedade_media = registros.aggregate(media=Avg('nivel_ansiedade'))['media']

    # Humor mais frequente no período
    humor_top = (
        registros.values('humor_emoji')
        .annotate(qtd=Count('humor_emoji'))
        .order_by('-qtd')
        .first()
    )
    humor_frequente = None
    if humor_top:
        humor_frequente = {
            'label': dict(RegistroHumor.Emoji.choices).get(humor_top['humor_emoji']),
            'qtd': humor_top['qtd'],
        }

    # Distribuição de cada humor (para uma lista simples com barras)
    distribuicao = []
    for valor, label in RegistroHumor.Emoji.choices:
        qtd = registros.filter(humor_emoji=valor).count()
        if qtd:
            distribuicao.append({
                'label': label,
                'qtd': qtd,
                'percentual': round((qtd / total) * 100) if total else 0,
            })
    distribuicao.sort(key=lambda d: d['qtd'], reverse=True)

    context = {
        'total': total,
        'ansiedade_media': round(ansiedade_media, 1) if ansiedade_media else None,
        'humor_frequente': humor_frequente,
        'distribuicao': distribuicao,
    }
    return render(request, 'humor/estatisticas.html', context)
