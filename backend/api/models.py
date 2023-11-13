from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    phone = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    created_date = models.DateTimeField(default=timezone.now)


class Brand(models.Model):
    name = models.CharField(max_length=100)


class ModelType(models.Model):
    name = models.CharField(max_length=100)


class Year(models.Model):
    year = models.CharField(max_length=4)


class Car(models.Model):

    STATES = (
        (0, 'MG'),
        (1, 'RJ'),
        (2, 'SP'),
    )

    TRANSMISSION = (
        (0, 'Automatic'),
        (1, 'Manual'),
    )

    FUEL = (
        (0, 'Diesel'),
        (1, 'Flex'),
        (2, 'Gasoline'),
        (3, 'Regular Gasoline'),
        (2, 'Electric'),
        (2, 'Hybrid'),
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand_id = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, blank=True, null=True
    )
    model_id = models.ForeignKey(
        ModelType, on_delete=models.SET_NULL, blank=True, null=True
    )
    year_id = models.ForeignKey(
        Year, on_delete=models.SET_NULL, blank=True, null=True
    )
    location = models.PositiveSmallIntegerField(choices=STATES)
    transmission = models.PositiveSmallIntegerField(choices=TRANSMISSION)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    mileage = models.FloatField()
    color = models.CharField(max_length=100)
    seat = models.PositiveSmallIntegerField()
    fuel = models.PositiveSmallIntegerField(choices=FUEL)
    created_date = models.DateField(default=timezone.now)
    activate = models.BooleanField(default=False)
    main_image = models.URLField()


class CarImages(models.Model):
    name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    image_url = models.URLField()
