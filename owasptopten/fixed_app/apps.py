from django.apps import AppConfig


class FixedAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fixed_app'