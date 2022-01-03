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

        car_id = request_body['car']
        customer_id = request_body['customer']

        response = update_car_name.apply_async(kwargs={"car_id": car_id, "customer_id": customer_id})
        result = response.get()

        if result == "success":
            response_body = result
            response_body["data"] = request_body
            return Response(response_body, status=status.HTTP_201_CREATED)
        return Response(result, status=status.HTTP_400_BAD_REQUEST)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
