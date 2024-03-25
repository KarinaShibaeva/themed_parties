# Generated by Django 3.2 on 2024-03-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appeal',
            name='course_name',
        ),
        migrations.AddField(
            model_name='appeal',
            name='events_name',
            field=models.CharField(choices=[('Прямиком в лето', 'Прямиком в лето')], default=1, max_length=128, verbose_name='Название курса'),
            preserve_default=False,
        ),
    ]