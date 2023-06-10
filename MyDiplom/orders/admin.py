from django.contrib import admin
from orders.models import Order

# class CatalogAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name = 'Каталог'
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = (
        'id', 'created',
        ('first_name', 'last_name'),
        ('email', 'address'),
        'basket_history', 'status', 'initiator',
    )
    readonly_fields = ('id', 'created')
