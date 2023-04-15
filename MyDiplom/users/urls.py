"""Определяет схемы URL для пользователей."""

from django.urls import path, include
from .views import RegisterUser

app_name = 'users'

urlpatterns = [
    # Включить URL авторизации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации
    path('register/', RegisterUser.as_view(), name='register'),
]