from django.apps import AppConfig


class AppsConfig():

    def ready(self):
        import movies.signals


class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'
    
    def ready(self):
        import movies.signals