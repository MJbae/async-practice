from rest_framework import viewsets
from .models import *
from .serializers import *


class CarRentalViewSet(viewsets.ModelViewSet):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
