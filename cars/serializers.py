from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRental
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)

    class Meta:
        model = Owner
        fields = "__all__"
