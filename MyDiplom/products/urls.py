"""Определяет схемы URL для products."""

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Домашняя страница
    path('', views.main_page, name='main_page'),
    # Страница каталога продуктов
    path('catalogs/', views.catalogs, name='catalogs'),
    path('catalogs/<int:catalog_id>/', views.catalog, name='catalog'),
    # Страница о магазине
    path('about_us/', views.about_us, name='about_us'),
    # Страница с контактами
    path('contacts/', views.contacts, name='contacts'),
    # Страница корзины
    path('basket/', views.basket, name='basket'),
    path('basket_item/', views.basket_item, name='basket_item'),
]
