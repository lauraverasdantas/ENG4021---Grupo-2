from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import ContatoConfianca


@login_required
def cadastrar_contato(request):
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
        return render(request, 'contatoconfianca/cadastrar_contato.html', {
            'contato': contato_existente,
            'opcoes_relacao': ContatoConfianca.Relacao.choices,
        })

    nome    = (request.POST.get('nome_contato') or '').strip()
    telefone = (request.POST.get('telefone') or '').strip()
    relacao  = (request.POST.get('relacao') or '').strip()

    if not nome or not telefone or not relacao:
        messages.error(request, 'Preencha todos os campos.')
        return render(request, 'contatoconfianca/cadastrar_contato.html', {
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
    return redirect('humor:humor')
