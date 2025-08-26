from django.apps import AppConfig

class HistoryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Correct the name to match what is in INSTALLED_APPS
    name = 'history'

    def ready(self):
        # Import the signals so they are registered with Django
        import history.signals
