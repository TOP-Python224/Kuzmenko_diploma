from .models import Catalog, Product
from users.models import User
from .models import Basket, BasketItem
from django.shortcuts import render


def main_page(request):
    """Домашняя страница интернет-магазина."""
    return render(request, 'main_page.html')


def catalogs(request):
    """Выводит каталоги продуктов."""
    catalogs = Catalog.objects.all()
    context = {'catalogs': catalogs}
    return render(request, 'catalogs.html', context)


def catalog(request, catalog_id):
    """Выводит определенный каталог продуктов."""
    catalog = Catalog.objects.get(id=catalog_id)
    products = Product.objects.filter(catalog_id=catalog_id)
    context = {'catalog': catalog, 'products': products}
    return render(request, 'catalog.html', context)


def about_us(request):
    """Выводит страничку о продавце."""
    return render(request, 'about_us.html')


def contacts(request):
    """Выводит страничку с контактами магазина."""
    return render(request, 'contacts.html')

def basket_item(request):
    """Выводит страничку ..."""
    # print(request.POST['product_id', 'product_name'])
    # b = Basket()
    # b.save()

    return render(request, 'catalog.html')

def basket(request):
    """Выводит страничку с корзиной."""
    b = BasketItem.objects.all()

    context = {'basket': b}
    return render(request, 'basket.html', context)
