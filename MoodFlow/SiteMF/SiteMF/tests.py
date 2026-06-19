from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class CriseViewTest(TestCase):
    def setUp(self):
        self.url = reverse('crise:crise')
        self.usuario = User.objects.create_user(
            username='teste', password='senha12345'
        )

    def test_redireciona_anonimo_para_login(self):
        resposta = self.client.get(self.url)
        self.assertEqual(resposta.status_code, 302)
        self.assertIn('login', resposta.url.lower())

    def test_usuario_logado_acessa(self):
        self.client.login(username='teste', password='senha12345')
        resposta = self.client.get(self.url)
        self.assertEqual(resposta.status_code, 200)
