# Import necessary modules and classes
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import UserSerializer, DeliverySerializer, AddressSerializer, ParcelSerializer, CarPartSerializer, FavoriteSerializer
from .models import *

@require_http_methods(["GET"])
def car_part_details(request, id):
    car_part = get_object_or_404(CarPart, id=id)
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
def car_part_detail_view(request, pk):
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
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class CarPartViewSet(viewsets.ModelViewSet):
    queryset = CarPart.objects.all()
    serializer_class = CarPartSerializer

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = FavoriteSerializer