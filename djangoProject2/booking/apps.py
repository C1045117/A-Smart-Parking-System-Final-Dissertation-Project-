from django.apps import AppConfig

class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'

    def ready(self):
        from .management.commands import init_images, process_images
        init_images.Command().handle()
        process_images.Command().handle()
