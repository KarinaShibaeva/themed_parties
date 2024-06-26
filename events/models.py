from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

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

    def __str__(self):
        return self.name


class Booking(models.Model):
    STATUS_CHOICE = (
        ("В обработке", "В обработке"),
        ("Выполнено", "Выполнено"),
        ("Отклонено", "Отклонено")
    )

    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    number_of_people = models.IntegerField(verbose_name='Количество человек')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, verbose_name='Статус', default='В обработке', choices=STATUS_CHOICE)


    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def get_total_price(self, *args, **kwargs):
        self.total_price = self.event.price * self.number_of_people
        super(Booking, self).save(*args, **kwargs)

@receiver(pre_save, sender=Booking)
def save_reservation_status(sender, instance, **kwargs):
    if instance.pk:
        db_instance = Booking.objects.get(pk=instance.pk)
        instance._old_status = db_instance.status
    else:
        instance._old_status = instance.status

@receiver(post_save, sender=Booking)
def send_notification(sender, instance, created, **kwargs):
    if created or instance.status != instance._old_status:
        subject = 'Изменение статуса бронирования'
        message = f'Статус бронирования был изменен на {instance.status}.'
        send_mail(subject, message, 'allevents.com', [instance.user.email])

class Comment(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

