from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    Group,
    Permission,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .utils.account_manager import CustomAccountManager


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='api_user_groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='api_user_permissions',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    objects = CustomAccountManager()


class Brand(models.Model):
    name = models.CharField(max_length=100)


class Year(models.Model):
    year = models.CharField(max_length=4)


class ModelType(models.Model):
    name = models.CharField(max_length=100)
    brand_id = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, blank=True, null=True
    )
    year_id = models.ForeignKey(
        Year, on_delete=models.SET_NULL, blank=True, null=True
    )
    category = models.CharField(max_length=100)


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

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
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
    about = models.TextField(max_length=500, blank=True, null=True)


class CarImages(models.Model):
    name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    image_url = models.URLField()
