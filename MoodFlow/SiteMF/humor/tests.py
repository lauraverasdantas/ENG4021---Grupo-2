from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase

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
