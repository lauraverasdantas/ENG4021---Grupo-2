from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class RegistroHumor(models.Model):
    """
    Uma entrada do diário de humor do usuário.

    Traduz a tabela Registros_Humor (Sprint 5 / banco_de_dados.sql) para o ORM
    do Django. O usuário é o model de autenticação padrão (settings.AUTH_USER_MODEL),
    conforme decidido na tarefa 1b.
    """

    class Emoji(models.IntegerChoices):
        NORMAL = 1, "Normal"
        TRISTE = 2, "Triste"
        FELIZ = 3, "Feliz"
        ESPERANCOSO = 4, "Esperançoso"
        RAIVOSO = 5, "Raivoso"
        APAIXONADO = 6, "Apaixonado"
        PREOCUPADO = 7, "Preocupado"
        ANSIOSO = 8, "Ansioso"
        ENTEDIADO = 9, "Entediado"

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="registros_humor",
    )
    data_hora = models.DateTimeField(auto_now_add=True)
    nivel_ansiedade = models.PositiveSmallIntegerField(
        help_text="Nível de ansiedade de 1 a 10.",
    )
    humor_emoji = models.PositiveSmallIntegerField(
        choices=Emoji.choices,
        help_text="Humor representado por um emoji (1 a 9).",
    )
    texto_livre = models.TextField(blank=True)

    class Meta:
        verbose_name = "Registro de Humor"
        verbose_name_plural = "Registros de Humor"
        ordering = ["-data_hora"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(nivel_ansiedade__gte=1)
                & models.Q(nivel_ansiedade__lte=10),
                name="nivel_ansiedade_entre_1_e_10",
            ),
            models.CheckConstraint(
                condition=models.Q(humor_emoji__gte=1) & models.Q(humor_emoji__lte=9),
                name="humor_emoji_entre_1_e_9",
            ),
        ]

    def __str__(self):
        return f"{self.usuario} — {self.get_humor_emoji_display()} ({self.data_hora:%d/%m/%Y %H:%M})"
