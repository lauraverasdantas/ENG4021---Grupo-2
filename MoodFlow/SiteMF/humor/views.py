from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from contatoconfianca.models import ContatoConfianca


@login_required
def humor(request):
    # Busca o contato de confiança do usuário logado (pode ser None)
    contato = (
        ContatoConfianca.objects
        .filter(usuario=request.user)
        .first()
    )
    return render(request, 'humor/humor.html', {'contato': contato})
