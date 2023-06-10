from django.contrib.auth.models import AbstractUser
from django.db import models


# ИСПРАВИТЬ: модель пользователя должна быть связана с django.contrib.auth.User
#       https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model
#   или наследовать от django.contrib.aut.AbstractUser (или django.contrib.aut.AbstractBaseUser)
#       https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model
#   если только не хотите переписывать четверть фреймворка
class User(AbstractUser):
    phone = models.CharField(max_length=18)

    def __str__(self):
        return f'{self.username}'

