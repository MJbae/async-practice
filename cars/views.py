from rest_framework import viewsets, status
from .models import *
from rest_framework.response import Response
from rest_framework.views import exceptions
from .serializers import *


class CarRentalViewSet(viewsets.ModelViewSet):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer

    def create(self, request, *args, **kwargs):
        request_body = request.data
        many = isinstance(request_body, list)

        car_id = request_body['car']
        customer_id = request_body['customer']

        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            raise exceptions.ParseError("car_id가 올바르지 않습니다.")

        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            raise exceptions.ParseError("customer_id가 올바르지 않습니다.")

        car.name = customer.name + "'s " + car.name
        car.save()

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
