from django.apps import AppConfig
import threading

class BookingAppConfig(AppConfig):
    name = 'booking_app'

    def ready(self):
        from .tasks import start_update_thread
        start_update_thread()
