from rest_framework import serializers

from config import settings
from .models import *
from django.core.validators import MaxLengthValidator, ProhibitNullCharactersValidator


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
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


class UnfilledTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class FilledTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        extra_kwargs = {
            """Non editable fields"""
            'creation_date': {'read_only': True},
            'payment_intent_id': {'read_only': True},
            'payment_status': {'read_only': True},
        }


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"
