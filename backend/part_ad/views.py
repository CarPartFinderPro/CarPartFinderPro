"""
This module contains views for the Part-AD API
"""

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import (
    UserSerializer,
    DeliverySerializer,
    AddressSerializer,
    ParcelSerializer,
    CarPartSerializer,
    FavoriteSerializer,
)
from .models import User, Delivery, Address, Parcel, CarPart, Favorite


# Define views

@require_http_methods(["GET"])
def car_part_details(car_part_id):
    """
    Returns car part details in JSON format
    """
    car_part = get_object_or_404(CarPart, id=car_part_id)
    data = {
        'id': car_part.id,
        'title': car_part.title,
        'brand': car_part.brand,
        'model': car_part.model,
        'year_from': car_part.year_from,
        'price': car_part.price,
        'description': car_part.description
    }
    return JsonResponse(data)


@api_view(['GET'])
def car_part_detail_view(pk):
    """
    Returns car part details in JSON format
    """
    car_part = get_object_or_404(CarPart, pk=pk)
    return JsonResponse({
        'id': car_part.id,
        'title': car_part.title,
        'brand': car_part.brand,
        'model': car_part.model,
        'year_from': car_part.year_from,
        'price': car_part.price
    })


# Define ViewSets for the models

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows deliveries to be viewed or edited.
    """
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows addresses to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CarPartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car parts to be viewed or edited.
    """
    queryset = CarPart.objects.all()
    serializer_class = CarPartSerializer


class ParcelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parcels to be viewed or edited.
    """
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows favorites to be viewed or edited.
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
