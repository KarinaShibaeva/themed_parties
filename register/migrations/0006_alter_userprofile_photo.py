# Generated by Django 5.0.4 on 2024-04-08 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='profile.png', upload_to='media/'),
        ),
    ]