from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import URLField
from account.models import *
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Shop(models.Model):
    SHOP_TYPES = [
        ('R', 'Restaurant'),
        ('C', 'Cafe'),
    ]
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    main_photo = models.ImageField(blank=True)
    phone = PhoneNumberField(null=True, blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    shop_type = models.CharField(blank=True, choices=SHOP_TYPES, max_length=1)
    site = models.URLField(blank=True)
    ispermited = models.BooleanField(default=False)

    sit_over4_max = models.IntegerField()
    sit_4_max = models.IntegerField()
    sit_2_max = models.IntegerField()

    sit_over4 = models.IntegerField()
    sit_4 = models.IntegerField()
    sit_2 = models.IntegerField()

class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Review(TimeStamedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)