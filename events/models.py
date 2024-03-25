from django.db import models
from embed_video.fields import EmbedVideoField


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

