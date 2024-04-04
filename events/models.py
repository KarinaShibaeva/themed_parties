from django.db import models

from register.models import CustomUser


class Topic(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField(max_length=128, verbose_name='Названние')
    description = models.TextField(verbose_name='Описание')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тематика')
    image = models.ImageField(upload_to="%Y/%m/%d", verbose_name='Изображение')
    video = models.CharField(max_length=128, verbose_name='Видео')
    date = models.DateTimeField(verbose_name='Дата проведения')
    place = models.CharField(max_length=128, verbose_name='Место проведения')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    seats = models.CharField(max_length=128, verbose_name='Количество мест')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Booking(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number_of_people = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def get_total_price(self, *args, **kwargs):
        self.total_price = self.event.price * self.number_of_people
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.name} - {self.event.name}'

