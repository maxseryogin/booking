from django.contrib import admin
from . models import Location, ParkingSpot, Booking

# Register your models here.
admin.site.register(Location)
admin.site.register(ParkingSpot)
admin.site.register(Booking)