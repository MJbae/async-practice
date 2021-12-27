import string
from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    code = models.CharField(max_length=3, null=False, blank=False, unique=True)
    symbol = models.CharField(max_length=5, null=False, blank=False, default='$')

    def __str__(self) -> str:
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self) -> str:
        return self.name
