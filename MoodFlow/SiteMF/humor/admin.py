from django.contrib import admin
from .models import RegistroHumor

<<<<<<< Updated upstream
=======
<<<<<<< HEAD
# Register your models here.

from humor.models import RegistroHumor

admin.site.register(RegistroHumor)
=======
>>>>>>> Stashed changes
@admin.register(RegistroHumor)
class RegistroHumorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'get_humor_emoji_display', 'nivel_ansiedade', 'data_hora')
    list_filter = ('humor_emoji', 'data_hora')
    search_fields = ('usuario__username', 'texto_livre')
    date_hierarchy = 'data_hora'
    readonly_fields = ('data_hora',)
<<<<<<< Updated upstream
=======
>>>>>>> d91b3f3361dc02843c5e094f05c0a09af5c8afef
>>>>>>> Stashed changes
