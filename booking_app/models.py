from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)

class ParkingSpot(models.Model):
    number = models.CharField(max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=True)  # Добавляем атрибут is_free

    def __str__(self):
        return self.number

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    confirmed = models.BooleanField(default=True)