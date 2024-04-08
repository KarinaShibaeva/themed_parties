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
        super().save(*args, **kwargs)
        if len(UserProfile.objects.filter(user=self)) == 0:
            UserProfile.objects.create(user=self)



class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/', default='profile.png')





