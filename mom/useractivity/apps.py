from django.apps import AppConfig


class UseractivityConfig(AppConfig):
    name = 'useractivity'

    def ready(self):
        from useractivity import signals