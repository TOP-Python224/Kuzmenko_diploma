from django.shortcuts import render


def main_page(request):
    """Домашняя страница интернет-магазина."""
    return render(request, 'main_page.html')

def catalog(request):
    """Выводит каталог продуктов."""
    return render(request, 'catalog.html')

def about_us(request):
    """Выводит каталог продуктов."""
    return render(request, 'about_us.html')
