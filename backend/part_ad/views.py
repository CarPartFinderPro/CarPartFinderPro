from django.http import JsonResponse
import json

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