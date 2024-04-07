# Generated by Django 3.2 on 2024-04-07 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тематика',
                'verbose_name_plural': 'Тематики',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Названние')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='%Y/%m/%d', verbose_name='Изображение')),
                ('video', models.CharField(max_length=128, verbose_name='Видео')),
                ('date', models.DateTimeField(verbose_name='Дата проведения')),
                ('place', models.CharField(max_length=128, verbose_name='Место проведения')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('seats', models.CharField(max_length=128, verbose_name='Количество мест')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.topic', verbose_name='Тематика')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=128, verbose_name='Имя')),
                ('surname', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=128, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=15)),
                ('number_of_people', models.IntegerField(verbose_name='Количество человек')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирования',
            },
        ),
    ]
