# Generated by Django 5.0.6 on 2024-06-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='Telegram ID'),
        ),
    ]