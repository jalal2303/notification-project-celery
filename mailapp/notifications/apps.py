from django.apps import AppConfig

class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailapp.notifications'
    
    def ready(self):
        # Import tasks to ensure they're registered
        from mailapp.notifications import tasks   # noqa