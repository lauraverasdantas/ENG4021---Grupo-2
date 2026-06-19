from datetime import date

from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse

from .models import RegistroHumor

User = get_user_model()


class RegistroHumorModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='teste', password='senha12345'
        )

    def test_cria_registro_valido(self):
        registro = RegistroHumor.objects.create(
            usuario=self.usuario,
            nivel_ansiedade=5,
            humor_emoji=RegistroHumor.Emoji.FELIZ,
            texto_livre='Dia tranquilo.',
        )
        self.assertEqual(registro.nivel_ansiedade, 5)
        self.assertEqual(registro.get_humor_emoji_display(), 'Feliz')

    def test_ansiedade_acima_do_limite_e_rejeitada(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                RegistroHumor.objects.create(
                    usuario=self.usuario,
                    nivel_ansiedade=11,
                    humor_emoji=RegistroHumor.Emoji.NORMAL,
                )

    def test_ansiedade_abaixo_do_limite_e_rejeitada(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                RegistroHumor.objects.create(
                    usuario=self.usuario,
                    nivel_ansiedade=0,
                    humor_emoji=RegistroHumor.Emoji.NORMAL,
                )

    def test_emoji_invalido_e_rejeitado(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                RegistroHumor.objects.create(
                    usuario=self.usuario,
                    nivel_ansiedade=5,
                    humor_emoji=99,
                )

    def test_ordenacao_mais_recente_primeiro(self):
        antigo = RegistroHumor.objects.create(
            usuario=self.usuario, nivel_ansiedade=3,
            humor_emoji=RegistroHumor.Emoji.TRISTE,
        )
        novo = RegistroHumor.objects.create(
            usuario=self.usuario, nivel_ansiedade=7,
            humor_emoji=RegistroHumor.Emoji.FELIZ,
        )
        registros = list(RegistroHumor.objects.all())
        self.assertEqual(registros[0], novo)
        self.assertEqual(registros[1], antigo)


class SalvarHumorViewTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='teste', password='senha12345'
        )
        self.url = reverse('humor:humor')
        self.client.login(username='teste', password='senha12345')

    def test_post_valido_cria_registro(self):
        resposta = self.client.post(self.url, {
            'humor_emoji': 3,
            'nivel_ansiedade': 4,
            'texto_livre': 'Tudo bem hoje.',
        })
        self.assertEqual(RegistroHumor.objects.count(), 1)
        registro = RegistroHumor.objects.first()
        self.assertEqual(registro.usuario, self.usuario)
        self.assertEqual(registro.humor_emoji, 3)
        self.assertEqual(registro.nivel_ansiedade, 4)
        self.assertEqual(resposta.status_code, 302)  # redireciona ao calendário

    def test_post_sem_emoji_nao_cria_registro(self):
        self.client.post(self.url, {
            'nivel_ansiedade': 4,
            'texto_livre': 'Sem humor.',
        })
        self.assertEqual(RegistroHumor.objects.count(), 0)

    def test_post_ansiedade_invalida_nao_cria_registro(self):
        self.client.post(self.url, {
            'humor_emoji': 3,
            'nivel_ansiedade': 50,
        })
        self.assertEqual(RegistroHumor.objects.count(), 0)


class HistoricoViewTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='teste', password='senha12345'
        )
        self.outro = User.objects.create_user(
            username='outro', password='senha12345'
        )
        RegistroHumor.objects.create(
            usuario=self.usuario, nivel_ansiedade=5,
            humor_emoji=RegistroHumor.Emoji.FELIZ,
        )
        RegistroHumor.objects.create(
            usuario=self.outro, nivel_ansiedade=5,
            humor_emoji=RegistroHumor.Emoji.TRISTE,
        )
        self.url = reverse('humor:historico')

    def test_exige_login(self):
        resposta = self.client.get(self.url)
        self.assertEqual(resposta.status_code, 302)

    def test_mostra_apenas_registros_do_usuario(self):
        self.client.login(username='teste', password='senha12345')
        resposta = self.client.get(self.url)
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.context['total'], 1)

    def test_filtro_por_emoji(self):
        self.client.login(username='teste', password='senha12345')
        resposta = self.client.get(self.url, {'emoji': RegistroHumor.Emoji.TRISTE})
        self.assertEqual(resposta.context['total'], 0)


class EstatisticasViewTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='teste', password='senha12345'
        )
        self.url = reverse('humor:estatisticas')

    def test_exige_login(self):
        resposta = self.client.get(self.url)
        self.assertEqual(resposta.status_code, 302)

    def test_sem_registros(self):
        self.client.login(username='teste', password='senha12345')
        resposta = self.client.get(self.url)
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.context['total'], 0)

from .models import RegistroHumor

User = get_user_model()


class RegistroHumorModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='teste', password='senha12345'
        )

    def test_cria_registro_valido(self):
        registro = RegistroHumor.objects.create(
            usuario=self.usuario,
            nivel_ansiedade=5,
            humor_emoji=RegistroHumor.Emoji.FELIZ,
            texto_livre='Dia tranquilo.',
        )
        self.assertEqual(registro.nivel_ansiedade, 5)
        self.assertEqual(registro.get_humor_emoji_display(), 'Feliz')

    def test_ansiedade_acima_do_limite_e_rejeitada(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                RegistroHumor.objects.create(
                    usuario=self.usuario,
                    nivel_ansiedade=11,
                    humor_emoji=RegistroHumor.Emoji.NORMAL,
                )

    def test_ansiedade_abaixo_do_limite_e_rejeitada(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                RegistroHumor.objects.create(
                    usuario=self.usuario,
                    nivel_ansiedade=0,
                    humor_emoji=RegistroHumor.Emoji.NORMAL,
                )

    def
