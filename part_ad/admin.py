from django.contrib import admin

from part_ad.models import (User, Parcel, Delivery, CarPart, Address)

# Register your models here.
admin.site.register(User)
admin.site.register(Parcel)
admin.site.register(Delivery)
admin.site.register(CarPart)
admin.site.register(Address)
