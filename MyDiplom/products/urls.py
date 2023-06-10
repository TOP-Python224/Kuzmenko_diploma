"""Определяет схемы URL для products."""

from django.urls import path
from . import views
from .views import MainPageView, ProductsListView, CatalogsListView

app_name = 'products'

urlpatterns = [
    # Домашняя страница
    # path('', views.main_page, name='main_page'),
    path('', MainPageView.as_view(), name='main_page'),
    # Страница каталога продуктов
    path('catalogs/', CatalogsListView.as_view(), name='catalogs'),
    path('products/<int:catalog_id>/', ProductsListView.as_view(), name='products'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    # Страница о магазине
    path('about_us/', views.about_us, name='about_us'),
    # Страница с контактами
    path('contacts/', views.contacts, name='contacts'),
    # Страница корзины
    path('basket/', views.basket, name='basket'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]
