from django.contrib import admin
from products.models import Catalog, Product, Basket, BasketItem


admin.site.register(Catalog)
admin.site.register(Product)
admin.site.register(Basket)


class BasketItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']

admin.site.register(BasketItem)

