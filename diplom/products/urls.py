"""Определяет схемы URL для products."""

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Домашняя страница
    path('', views.main_page, name='main_page'),
    # Страница каталога продуктов
    path('catalog/', views.catalog, name='catalog'),
    # Страница о магазине
    path('about_us/', views.about_us, name='about_us'),
]
