from django.apps import AppConfig
from django.db.models.signals import post_migrate


class RegisterConfig(AppConfig):
    name = 'register'

    def ready(self):
        from .signals import create_superuser
        post_migrate.connect(create_superuser, sender=self)
