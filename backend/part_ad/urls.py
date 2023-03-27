# Import necessary modules and views.
from django.urls import path, include
from . import views
from rest_framework import routers
from part_ad.views import *

# Register the ViewSets with the default router.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'car_parts', CarPartViewSet)
router.register(r'parcel', ParcelViewSet)
router.register(r'delivery', DeliveryViewSet)
router.register(r'address', AddressViewSet)

# Define the URL patterns for the app.
urlpatterns = [
    # Map the API endpoints to the corresponding ViewSets.
    path('api/', include(router.urls)),
    path('api/car_parts/<int:id>/', views.car_part_details, name='car_part_details')
]