from django.shortcuts import render, get_object_or_404, redirect
from .models import ParkingSpot, Booking, BookingHistory
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
import logging
from pytz import timezone as pytz_timezone

logger = logging.getLogger(__name__)

# Главная страница
def home(request):
    status = request.GET.get('status')
    if status == 'free':
        parking_spots = ParkingSpot.objects.filter(is_free=True)
    elif status == 'occupied':
        parking_spots = ParkingSpot.objects.filter(is_free=False)
    else:
        parking_spots = ParkingSpot.objects.all()
    return render(request, 'home.html', {'parking_spots': parking_spots})

@login_required(login_url='/login/')
def my_bookings(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        action = request.POST.get('action')
        booking = get_object_or_404(Booking, id=booking_id, user=user)
        booking_history = BookingHistory.objects.filter(booking__user=request.user)
        context = {
                'bookings': bookings,
                'booking_history': booking_history,
            }
        if action == 'cancel':
            booking.parking_spot.is_free = True
            booking.parking_spot.save()
            BookingHistory.objects.create(
                booking=booking,
                action='cancelled',
                start_date=booking.start_date,
                end_date=booking.end_date,
                parking_spot_number=booking.parking_spot.number
            )
            booking.delete()
            return redirect('my_bookings')
        elif action == 'extend':
            booking.end_date += timezone.timedelta(days=1)
            booking.save()
            BookingHistory.objects.create(
                booking=booking,
                action='extended',
                start_date=booking.start_date,
                end_date=booking.end_date,
                parking_spot_number=booking.parking_spot.number
            )
            return redirect('my_bookings')

    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required(login_url='/login/')
def book_spot(request):
    selected_spot_id = request.GET.get('spot_id')  # Получаем идентификатор выбранного места
    if request.method == 'POST':
        spot_id = request.POST['spot']
        spot = get_object_or_404(ParkingSpot, id=spot_id)
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        booking = Booking.objects.create(
            user=request.user,
            parking_spot=spot,
            start_date=start_date,
            end_date=end_date,
            confirmed=True
        )
        BookingHistory.objects.create(
            booking=booking,
            action='created',
            start_date=booking.start_date,
            end_date=booking.end_date,
            parking_spot_number=booking.parking_spot.number
        )
        spot.is_free = False
        spot.save()
        return redirect('my_bookings')
    else:
        spots = ParkingSpot.objects.filter(is_free=True)
        return render(request, 'book_spot.html', {'spots': spots, 'selected_spot_id': selected_spot_id})