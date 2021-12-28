import string
from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    code = models.CharField(max_length=3, null=False, blank=False, unique=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, blank=True, related_name='cars')
    name = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self) -> str:
        return self.name + '_' + self.code


class CarRental(models.Model):
    code = models.CharField(max_length=3, null=False, blank=False)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.code
