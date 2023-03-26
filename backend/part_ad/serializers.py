# Importing serializers from Django REST framework
from rest_framework import serializers

# Importing all models that need to be serialized
from .models import User, Parcel, Delivery, Address, CarPart


# Serializer class for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Setting the model to be serialized
        model = User
        # Including all fields of the model
        fields = "__all__"

# Serializer class for Parcel model
class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        # Setting the model to be serialized
        model = Parcel
        # Including all fields of the model
        fields = "__all__"

# Serializer class for Delivery model
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        # Setting the model to be serialized
        model = Delivery
        # Including all fields of the model
        fields = "__all__"

# Serializer class for Address model
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        # Setting the model to be serialized
        model = Address
        # Including all fields of the model
        fields = "__all__"

# Serializer class for CarPart model
class CarPartSerializer(serializers.ModelSerializer):
    class Meta:
        # Setting the model to be serialized
        model = CarPart
        # Including all fields of the model
        fields = "__all__"