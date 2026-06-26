from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("SiteMF", "0002_perfilusuario"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContatoConfianca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_contato", models.CharField(max_length=120)),
                ("telefone", models.CharField(max_length=20)),
                (
                    "relacao",
                    models.CharField(
                        choices=[
                            ("familia", "Família"),
                            ("amigo", "Amigo(a)"),
                            ("parceiro", "Parceiro(a)"),
                            ("profissional", "Profissional"),
                            ("outro", "Outro"),
                        ],
                        max_length=20,
                    ),
                ),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=models.deletion.CASCADE,
                        related_name="contato_confianca",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Contato de Confiança",
                "verbose_name_plural": "Contatos de Confiança",
            },
        ),
    ]
