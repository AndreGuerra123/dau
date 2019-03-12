from django.apps import AppConfig
class DjangoAutoUserConfig(AppConfig):
    name = 'dau'
    verbose_name = "Django Auto User"
    def ready(self):
        from .core import DjangoAutoUser
        DjangoAutoUser()
    

