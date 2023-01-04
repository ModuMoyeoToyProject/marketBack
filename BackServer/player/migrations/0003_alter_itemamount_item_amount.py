# Generated by Django 4.1.1 on 2023-01-04 01:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_character_location_inventory_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemamount',
            name='item_amount',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)], verbose_name='수량 (1~999)'),
        ),
    ]
