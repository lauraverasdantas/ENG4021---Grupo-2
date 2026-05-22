from django import forms
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import Profile


User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = {
            "username": "Nome de usuario",
            "first_name": "Nome",
            "last_name": "Sobrenome",
            "email": "E-mail",
        }
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "readonly": "readonly",
                    "placeholder": "Seu nome de usuario",
                }
            ),
            "first_name": forms.TextInput(attrs={"placeholder": "Seu nome"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Seu sobrenome"}),
            "email": forms.EmailInput(attrs={"placeholder": "voce@exemplo.com"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].disabled = True

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip()
        if not email:
            return email

        email_exists = (
            User.objects.filter(email__iexact=email)
            .exclude(pk=self.instance.pk)
            .exists()
        )
        if email_exists:
            raise forms.ValidationError("Este e-mail ja esta em uso.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "bio", "phone_number", "birth_date", "location"]
        labels = {
            "image": "Foto do perfil",
            "bio": "Bio",
            "phone_number": "Telefone",
            "birth_date": "Data de nascimento",
            "location": "Cidade",
        }
        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Conte um pouco sobre voce",
                }
            ),
            "phone_number": forms.TextInput(attrs={"placeholder": "(11) 99999-9999"}),
            "birth_date": forms.DateInput(attrs={"type": "date"}),
            "location": forms.TextInput(attrs={"placeholder": "Cidade - UF"}),
        }

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birth_date")
        if birth_date and birth_date > timezone.localdate():
            raise forms.ValidationError("A data de nascimento nao pode estar no futuro.")
        return birth_date

    def clean_phone_number(self):
        return self.cleaned_data.get("phone_number", "").strip()

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return image

        valid_types = {"image/jpeg", "image/png", "image/webp"}
        content_type = getattr(image, "content_type", None)
        if content_type and content_type not in valid_types:
            raise forms.ValidationError("Envie uma imagem JPG, PNG ou WEBP.")

        if image.size > 2 * 1024 * 1024:
            raise forms.ValidationError("A imagem deve ter no maximo 2 MB.")

        return image
