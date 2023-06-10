"""Определяет схемы URL для пользователей."""
from django.urls import path
from .views import registerUser, profile, login, user_logout

app_name = 'users'

urlpatterns = [
    # Странички авторизации и выхода.
    path('login/', login, name='login'),
    path('logout/', user_logout, name='logout'),
    # Страницы регистрации и профиля.
    path('register/', registerUser, name='register'),
    path('profile/', profile, name='profile'),
]
