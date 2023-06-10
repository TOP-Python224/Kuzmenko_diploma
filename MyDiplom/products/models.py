from django.db import models


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



class BasketItem(models.Model):
    basket = models.OneToOneField(Basket, models.CASCADE, primary_key=True)
    product = models.ForeignKey('Product', models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket_item'
        unique_together = (('basket', 'product'),)

    def __str__(self):
        return f'{self.product} {self.quantity}'

