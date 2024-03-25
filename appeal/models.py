from django.db import models

class Appeal(models.Model):
    TYPES = (
        ('Прямиком в лето', 'Прямиком в лето'),
    )

    STATUS_CHOICE = (
        ("a", "В обработке"),
        ("b", "Выполнено"),
        ("c", "Отклонено")
    )

    events_name = models.CharField(choices=TYPES, max_length=128, verbose_name='Название курса')
    contact = models.CharField(max_length=128, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Электронная почта", blank=False)
    status = models.CharField(max_length=100, verbose_name='Статус', choices=STATUS_CHOICE)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    def __iter__(self):
        for field in self._meta.fields:
            yield field.verbose_name, field.value_to_string(self)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
