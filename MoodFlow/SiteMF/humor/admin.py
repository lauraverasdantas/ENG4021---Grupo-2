from django.contrib import admin
from .models import RegistroHumor

@admin.register(RegistroHumor)
class RegistroHumorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'get_humor_emoji_display', 'nivel_ansiedade', 'data_hora')
    list_filter = ('humor_emoji', 'data_hora')
    search_fields = ('usuario__username', 'texto_livre')
    date_hierarchy = 'data_hora'
    readonly_fields = ('data_hora',)
