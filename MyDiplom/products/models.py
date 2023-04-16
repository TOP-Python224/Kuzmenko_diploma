from django.db import models


class Catalog(models.Model):
    # ИСПРАВИТЬ здесь и далее: в Django ORM числовые автоинкрементирующиеся первичные ключи должны быть созданы с помощью AutoField и производных классов
    #   https://docs.djangoproject.com/en/4.1/topics/db/models/#automatic-primary-key-fields
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
    # КОММЕНТАРИЙ: можно ещё использовать ImageField и каталог MEDIA_ROOT
    #   https://docs.djangoproject.com/en/4.1/ref/models/fields/#imagefield
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
    # КОММЕНТАРИЙ: в Django ORM нет полноценной поддержки составных первичных ключей, поэтому с точки зрения фреймворка данное поле является единственным первичным ключом — а связь один-к-одному означает, что на каждую корзину будет приходиться один элемент, второй элемент в эту же корзину просто не сможет быть добавлен — вряд ли это желаемое поведение
    # ИСПРАВИТЬ: проще всего, пожалуй, добавить отдельное поле первичного ключа, а эти два поля оставить связанными ограничением UniqueConstraint — это из серии "забудьте про оптимизацию", но у вас не высоконагруженное приложение, так что сойдёт
    basket = models.OneToOneField(Basket, models.CASCADE, primary_key=True)
    product = models.ForeignKey(Product, models.CASCADE)
    # ИСПРАВИТЬ: создание экземпляра BasketItem должно означать, что у вас уже ненулевое количество товара в корзине — default=1 куда лучше подойдёт вместо blank=True и null=True
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket_item'
        unique_together = (('basket', 'product'),)

    def __str__(self):
        return f'{self.product} {self.quantity}'

