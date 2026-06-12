import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoConfianca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_contato', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('relacao', models.CharField(
                    choices=[
                        ('Psicólogo',   'Psicólogo'),
                        ('Familiar',    'Familiar'),
                        ('Amigo',       'Amigo'),
                        ('Namorado(a)', 'Namorado(a)'),
                        ('Outro',       'Outro'),
                    ],
                    default='Amigo',
                    max_length=20,
                )),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='contatos_confianca',
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={
                'verbose_name': 'Contato de Confiança',
                'verbose_name_plural': 'Contatos de Confiança',
                'ordering': ['nome_contato'],
            },
        ),
    ]
