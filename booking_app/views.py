from django.shortcuts import render, get_object_or_404, redirect
from .models import ParkingSpot, Booking
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse

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

        if action == 'cancel':
            booking.parking_spot.is_free = True
            booking.parking_spot.save()
            booking.delete()
            return redirect('my_bookings')
        elif action == 'extend':
            booking.end_date += timezone.timedelta(days=1)  # Пример продления на 1 день
            booking.save()
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
        Booking.objects.create(
            user=request.user,
            parking_spot=spot,
            start_date=start_date,
            end_date=end_date,
            confirmed=True
        )
        # Обновляем статус парковочного места
        spot.is_free = False
        spot.save()
        return redirect('my_bookings')
    else:
        spots = ParkingSpot.objects.filter(is_free=True)
        return render(request, 'book_spot.html', {'spots': spots, 'selected_spot_id': selected_spot_id})