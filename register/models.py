from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=128, verbose_name='Имя')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, verbose_name='Пароль')
    password_confirm = models.CharField(max_length=128, verbose_name='Подтверждение пароля')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]