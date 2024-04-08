# Generated by Django 5.0.4 on 2024-04-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_comment_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('a', 'В обработке'), ('b', 'Выполнено'), ('c', 'Отклонено')], default='a', max_length=100, verbose_name='Статус'),
        ),
    ]
