from rest_framework import viewsets, status
from .models import *
from rest_framework.response import Response
from rest_framework.views import exceptions
from .serializers import *
from .tasks import update_car_name
import time


class CarRentalViewSet(viewsets.ModelViewSet):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer

    def create(self, request, *args, **kwargs):
        request_body = request.data
        many = isinstance(request_body, list)

        car_id = request_body['car']
        customer_id = request_body['customer']

        update_car_name.delay(car_id, customer_id)

        serializer = CarRentalSerializer(data=request_body, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
