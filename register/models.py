from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('P', 'Посетитель'),
        ('O', 'Организатор'),
    )
    name = models.CharField(max_length=128, verbose_name='Имя')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, verbose_name='Пароль')
    account_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default='P', verbose_name='Тип аккаунта')

