from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("SiteMF", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PerfilUsuario",
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
                ("data_nasc", models.DateField()),
                ("telefone", models.CharField(max_length=20)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=models.deletion.CASCADE,
                        related_name="perfil",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Perfil de Usuário",
                "verbose_name_plural": "Perfis de Usuários",
            },
        ),
    ]