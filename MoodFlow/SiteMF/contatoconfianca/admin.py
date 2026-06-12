from django.contrib import admin
from .models import ContatoConfianca


@admin.register(ContatoConfianca)
class ContatoConfiancaAdmin(admin.ModelAdmin):
    list_display = ('nome_contato', 'relacao', 'telefone', 'usuario', 'criado_em')
    list_filter  = ('relacao',)
    search_fields = ('nome_contato', 'usuario__username')
