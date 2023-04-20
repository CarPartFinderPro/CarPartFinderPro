"""
This module defines URL patterns for the Part-AD app.
"""

from django.urls import path, include
from rest_framework import routers
from .views import (
    UserViewSet,
    CarPartViewSet,
    ParcelViewSet,
    DeliveryViewSet,
    AddressViewSet,
    FavoriteViewSet,
    car_part_details,
    car_part_detail_view,
)

# Register the ViewSets with the default router.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'car_parts', CarPartViewSet)
router.register(r'parcel', ParcelViewSet)
router.register(r'delivery', DeliveryViewSet)
router.register(r'address', AddressViewSet)
router.register(r'favorite', FavoriteViewSet)

# Define the URL patterns for the app.
urlpatterns = [
    # Map the API endpoints to the corresponding ViewSets.
    path('api/', include(router.urls)),
    path('api/car_parts/<int:id>/', car_part_details, name='car_part_details'),
    path('api/car_parts/<int:pk>/', car_part_detail_view, name='car_part_detail_view')
]
