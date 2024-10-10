import os
import django
from datetime import datetime, timedelta

# Установите настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking_project.settings')
django.setup()

from booking_app.models import ParkingSpot, Location

# Получите существующую локацию или создайте новую
location, created = Location.objects.get_or_create(name='Main Location')

# Добавьте 12 парковочных места
for i in range(1, 13):
    # Установите время, до которого место свободно (например, на 7 дней вперед)
    free_until = datetime.now() + timedelta(days=1)
    ParkingSpot.objects.create(number=f'Место {i}', location=location, is_free=True)

print("12 парковочных места добавлены в базу данных.")
