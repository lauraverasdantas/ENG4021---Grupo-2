from django.apps import AppConfig


class EditarperfilConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "editarperfil"

    def ready(self):
        import editarperfil.signals  # noqa: F401
