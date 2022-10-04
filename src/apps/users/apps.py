from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "src.apps.users"
    verbose_name = "Users"

    def ready(self):
        from src.apps.users import signals  # NOQA
