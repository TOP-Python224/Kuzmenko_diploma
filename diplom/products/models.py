from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime


class PositiveTinyAutoField(models.AutoField):
    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if not (0 <= value < 256):
            raise ValidationError('value for this field should be between 0 and 255')
        return value

    def db_type(self, connection):
        return 'tinyint unsigned auto_increment'

    def rel_db_type(self, connection):
        return 'tinyint unsigned'


class Catalog(models.Model):
    id = PositiveTinyAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'catalogs'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # image - думаю какое правильнее поле к нему подобрать
    # еще не разорался как загружать в БД MySQL изображения и как их потом извлекать
    catalog_id = models.ForeignKey(Catalog, models.CASCADE)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f'{self.name}'

class Basket(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()

class BasketItem(models.Model):
    basket_id = models.IntegerField

# class AcceptedOrders(models.Model):
#     id = models.SmallIntegerField()
#     name = models.CharField(max_length=30)
#     surname = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)
#     phonenumber = models.CharField(max_length=30)
#     fullprice = models.DecimalField(max_digits=8, decimal_places=2)
#     date = models.DateField()
#     status = models.BooleanField()
#
#     class Meta:
#         db_table = 'accepted_orders'



# class User(models.Model, AbstractUser):

