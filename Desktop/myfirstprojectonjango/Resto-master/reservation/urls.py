from django.urls import path
from . import views


app_name = 'reservation'


urlpatterns = [
    path('', views.reserve, name='reserve'),
    path('reservations/', views.display_reservations, name='my-reservations'),
    path('get-all-reservations/', views.ReservationListAPIView.as_view(), name='get-all-orders'),
    path('create-reservation/', views.ReservationCreateAPIView.as_view(), name='create-reservation'),
]
