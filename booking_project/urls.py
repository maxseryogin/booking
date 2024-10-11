from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from booking_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('my_bookings/', views.my_bookings, name='my_bookings'),  # Страница "Мои бронирования"
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Страница логина
    path('book_spot/', views.book_spot, name='book_spot'),  # Бронирование парковочного места
    path('register/', views.register, name='register'),
]