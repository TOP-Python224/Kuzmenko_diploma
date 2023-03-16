from django.db import models
from datetime import datetime

# class Product(models.Model):
#     id = models.SmallIntegerField()
#     name = models.CharField(max_length=30)
#     description = models.CharField(max_length=150)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#
#     class Meta:
#         db_table = 'products'
#
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