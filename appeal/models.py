from django.db import models

from events.models import Events


class Appeal(models.Model):
    STATUS_CHOICE = (
        ("a", "В обработке"),
        ("b", "Выполнено"),
        ("c", "Отклонено")
    )

    events_name = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name='Название курса')
    contact = models.CharField(max_length=128, verbose_name="ФИО")
    seats = models.IntegerField()
    email = models.EmailField(verbose_name="Электронная почта", blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    status = models.CharField(max_length=100, verbose_name='Статус', choices=STATUS_CHOICE)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    def __iter__(self):
        for field in self._meta.fields:
            yield field.verbose_name, field.value_to_string(self)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
