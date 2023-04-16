from django.db import models


# ИСПРАВИТЬ: модель пользователя должна быть связана с django.contrib.auth.User
#       https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model
#   или наследовать от django.contrib.aut.AbstractUser (или django.contrib.aut.AbstractBaseUser)
#       https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model
#   если только не хотите переписывать четверть фреймворка
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return f'id: {self.id} Username: {self.username} Email: {self.email}'
