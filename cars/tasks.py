import json
from asyncio import exceptions
from django.db import transaction, IntegrityError
from cars.models import Car, Customer, CarRental
from config.celery import app
from celery import shared_task


@shared_task
def update_car_name(car_id, customer_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return {"result": "fail", "message": "car_id가 올바르지 않습니다."}

    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return {"result": "fail", "message": "customer_id가 올바르지 않습니다."}

    modified_name = f"{car.name}'s {customer.name}"
    car.name = modified_name
    car.save()

    rental = CarRental(code=str(car_id+customer_id), car=car, customer=customer)
    rental.save()

    return {"result": "success"}


@shared_task
def destroy_cars():
    first_id = Car.objects.earliest("id").__dict__["id"]
    last_id = Car.objects.latest("id").__dict__["id"]
    id_list = [car_id for car_id in range(first_id, last_id + 1)]
    try:
        _delete_all_in_bulk(id_list)
    except exceptions.InvalidStateError:
        return {"result": "fail"}

    return {"result": "success"}


def _delete_all_in_bulk(id_list):
    try:
        with transaction.atomic():
            Car.objects.filter(pk__in=id_list).delete()
    except IntegrityError:
        raise exceptions.InvalidStateError("데이터 삭제에 이상이 있습니다.")
