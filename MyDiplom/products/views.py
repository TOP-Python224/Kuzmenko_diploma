from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Catalog, Product
from .models import Basket
from django.shortcuts import render, HttpResponseRedirect



class MainPageView(TemplateView):
    """Домашняя страница интернет-магазина."""
    template_name = 'main_page.html'



class CatalogsListView(ListView):
    """Выводит каталоги продуктов."""
    model = Catalog
    template_name = 'catalogs.html'


# def products(request, catalog_id=None, page_number=1):
#     """Выводит определенный каталог продуктов."""
#     # catalog = Catalog.objects.get(id=catalog_id)
#     products = Product.objects.filter(catalog_id=catalog_id) if catalog_id else Product.objects.all()
#     per_page = 3
#     paginator = Paginator(products, per_page)
#     products_paginator = paginator.page(page_number)
#     # context = {'catalog': catalog, 'products': products_paginator}
#     context = {'products': products_paginator}
#     return render(request, 'products.html', context)



class ProductsListView(ListView):
    model = Product
    template_name = 'products.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        catalog_id = self.kwargs.get('catalog_id')
        return queryset.filter(catalog_id=catalog_id) if catalog_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['catalogs'] = Catalog.objects.all()
        return context



def about_us(request):
    """Выводит страничку о продавце."""
    return render(request, 'about_us.html')



def contacts(request):
    """Выводит страничку с контактами магазина."""
    return render(request, 'contacts.html')



def basket(request):
    """Выводит страничку с корзиной."""
    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(basket.sum() for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)
    context = {'baskets': baskets, 'total_sum': total_sum, 'total_quantity': total_quantity}
    return render(request, 'basket.html', context)



@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    q = basket.quantity
    if q > 1:
        Basket.objects.filter(id=basket_id).update(quantity=q-1)
    else:
        basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
