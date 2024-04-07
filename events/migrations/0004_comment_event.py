# Generated by Django 5.0.4 on 2024-04-07 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.events'),
            preserve_default=False,
        ),
    ]
