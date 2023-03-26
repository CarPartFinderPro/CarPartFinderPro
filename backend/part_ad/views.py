# Import necessary modules and classes
from django.http import JsonResponse
import json
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer, DeliverySerializer, AddressSerializer, ParcelSerializer, CarPartSerializer
from .models import *

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

# Define views to return JSON data from fixture files
def user_list(request):
    with open('fixtures/user_fixtures.json') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)

def address_list(request):
    with open('fixtures/address_fixtures.json') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)

def delivery_list(request):
    with open('fixtures/delivery_fixtures.json') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)

def parcel_list(request):
    with open('fixtures/parcel_fixtures.json') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)

def car_part_list(request):
    with open('fixtures/car_part_fixtures.json') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)