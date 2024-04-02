from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('P', 'Посетитель'),
        ('O', 'Организатор'),
    )
    name = models.CharField(max_length=128, verbose_name='Имя')
    email = models.EmailField(unique=True)
    account_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default='P', verbose_name='Тип аккаунта')
    email_verified = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not hasattr(self, 'profile'):
            UserProfile.objects.create(user=self)
        super().save(*args, **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


