from rest_framework import serializers

from config import settings
from .models import *
from django.core.validators import MaxLengthValidator


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'code', 'symbol']
        if settings.DEBUG:
            extra_kwargs = {
                'name': {
                    'validators': [MaxLengthValidator]
                },
                'code': {
                    'validators': [MaxLengthValidator]
                }
            }


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"
