from django.urls import path
from .views import home, booking, MenuView, BookingView

urlpatterns = [
    path('', home),
    path('booking/', booking),

    path('api/menu/', MenuView.as_view()),
    path('api/bookings/', BookingView.as_view()),
]