from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from editarperfil.models import Profile


User = get_user_model()


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(
        label="Nome completo",
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Ex: Maria Silva"}),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"placeholder": "maria@exemplo.com"}),
    )
    phone_number = forms.CharField(
        label="Telefone",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "(11) 99999-9999"}),
    )
    birth_date = forms.DateField(
        label="Data de nascimento",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "full_name",
            "birth_date",
            "email",
            "phone_number",
            "username",
            "password1",
            "password2",
        ]
        labels = {
            "username": "Nome de usuario",
            "password1": "Senha",
            "password2": "Confirmar senha",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "mariasilva123"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"placeholder": "Crie uma senha forte"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Repita sua senha"})

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Este e-mail ja esta em uso.")
        return email

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birth_date")
        if birth_date and birth_date > timezone.localdate():
            raise forms.ValidationError("A data de nascimento nao pode estar no futuro.")
        return birth_date

    def clean_phone_number(self):
        return self.cleaned_data.get("phone_number", "").strip()

    def save(self, commit=True):
        user = super().save(commit=False)
        full_name = self.cleaned_data["full_name"].strip()
        first_name, _, last_name = full_name.partition(" ")
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.phone_number = self.cleaned_data.get("phone_number", "")
            profile.birth_date = self.cleaned_data.get("birth_date")
            profile.save(update_fields=["phone_number", "birth_date"])

        return user
