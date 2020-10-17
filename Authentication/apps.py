from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'Authentication'


    def ready(self):
        import Authentication.signals