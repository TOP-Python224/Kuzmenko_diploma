from django.db import models
from django.core.exceptions import ValidationError

# class PositiveTinyAutoField(models.AutoField):
#     def get_db_prep_value(self, value, connection, prepared=False):
#         value = super().get_db_prep_value(value, connection, prepared)
#         if not (0 <= value < 256):
#             raise ValidationError('value for this field should be between 0 and 255')
#         return value
#
#     def db_type(self, connection):
#         return 'tinyint unsigned auto_increment'
#
#     def rel_db_type(self, connection):
#         return 'tinyint unsigned'



class Catalog(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'catalog'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=100)
    catalog = models.ForeignKey(Catalog, models.CASCADE)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.catalog.name}'



class Basket(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'basket'

    def __str__(self):
        return f'{self.id} {self.created}'

# class Basket(models.Model):
#     id = models.IntegerField(primary_key=True)
#     created = models.DateTimeField()
#
#     class Meta:
#         db_table = 'basket'
#
#     def __str__(self):
#         return f'{self.id} {self.created}'
#

class BasketItem(models.Model):
    basket = models.OneToOneField(Basket, models.CASCADE, primary_key=True)
    product = models.ForeignKey('Product', models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket_item'
        unique_together = (('basket', 'product'),)


# class BasketItem(models.Model):
#     id = models.IntegerField(primary_key=True)
#     quantity = PositiveTinyAutoField
#     product_id = models.ForeignKey(Product, models.CASCADE)
#     basket_id = models.ForeignKey(Basket, models.CASCADE)
#     constraints = [models.UniqueConstraint(fields=[product_id, basket_id], name='unique_name')]
#
#     class Meta:
#         # unique_together = (('product_id', 'basket_id'),)
#         db_table = 'basket_item'
#
#
#     def __str__(self):
#         return f'{self.id}'




class BasketItem(models.Model):
    basket = models.OneToOneField(Basket, models.DO_NOTHING, primary_key=True)  # The composite primary key (basket_id, product_id) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket_item'
        unique_together = (('basket', 'product'),)
