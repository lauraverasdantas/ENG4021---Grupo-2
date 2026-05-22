from django.contrib.auth.forms import AuthenticationForm
from django import forms


class MoodFlowAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Nome de usuario",
        widget=forms.TextInput(
            attrs={
                "class": "input-field",
                "placeholder": "usuario",
                "autocomplete": "username",
            }
        ),
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "input-field",
                "placeholder": "senha",
                "autocomplete": "current-password",
            }
        ),
    )
