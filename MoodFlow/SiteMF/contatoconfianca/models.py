from django.conf import settings
from django.db import models


class ContatoConfianca(models.Model):
    """
    Contato de confiança do usuário, acionado no Modo Crise.
    Mapeia a tabela Contatos_Confianca do banco_de_dados.sql (Sprint 5).
    """

    class Relacao(models.TextChoices):
        PSICOLOGO  = 'Psicólogo',  'Psicólogo'
        FAMILIAR   = 'Familiar',   'Familiar'
        AMIGO      = 'Amigo',      'Amigo'
        NAMORADO   = 'Namorado(a)', 'Namorado(a)'
        OUTRO      = 'Outro',      'Outro'

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contatos_confianca',
    )
    nome_contato = models.CharField(max_length=100)
    telefone     = models.CharField(max_length=20)
    relacao      = models.CharField(
        max_length=20,
        choices=Relacao.choices,
        default=Relacao.AMIGO,
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contato de Confiança'
        verbose_name_plural = 'Contatos de Confiança'
        ordering = ['nome_contato']

    def __str__(self):
        return f"{self.nome_contato} ({self.relacao}) — {self.usuario}"
