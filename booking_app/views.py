from django.shortcuts import render, get_object_or_404, redirect
from .models import ParkingSpot, Booking
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required(login_url='/login/')
def book_spot(request, spot_id):
    spot = get_object_or_404(ParkingSpot, id=spot_id)
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        Booking.objects.create(
            user=request.user,
            parking_spot=spot,
            start_date=start_date,
            end_date=end_date,
            confirmed=True
        )
        return redirect('my_bookings')
    return render(request, 'book_spot.html', {'spot': spot})