from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.user_list, name='user_list'),
    path('api/addresses/', views.address_list, name='address_list'),
    path('api/deliveries/', views.delivery_list, name='delivery_list'),
    path('api/parcels/', views.parcel_list, name='parcel_list'),
    path('api/car_parts/', views.car_part_list, name='car_part_list'),
]