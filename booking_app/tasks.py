import threading
import time
from django.utils import timezone
from booking_app.models import ParkingSpot, Booking

thread_started = False

def start_update_thread():
    global thread_started
    if not thread_started:
        thread = threading.Thread(target=update_parking_spots)
        thread.daemon = True
        thread.start()
        thread_started = True

def update_parking_spots():
    while True:
        now = timezone.now() + timezone.timedelta(hours=3)
        print(f"Текущее время: {now}")
        
        # Обновляем статусы парковочных мест
        update_finished_bookings(now)
        update_current_bookings(now)
        print('Статусы парковочных мест обновлены')
        time.sleep(30)  # Ждем 30 секунд

def update_finished_bookings(now):
    bookings = Booking.objects.filter(end_date__lte=now)
    for booking in bookings:
        spot = booking.parking_spot
        print(f"Обновление статуса для места: {spot.number}")
        spot.is_free = True
        spot.free_until = None
        booking.delete()  # Сбрасываем free_until
        spot.save()

def update_current_bookings(now):
    bookings = Booking.objects.filter(start_date__lte=now, end_date__gte=now)
    for booking in bookings:
        spot = booking.parking_spot
        print(f"Обновление статуса для места: {spot.number}")
        spot.is_free = False
        spot.free_until = booking.end_date  # Устанавливаем free_until
        spot.save()
