# Generated by Django 4.1.1 on 2023-01-09 05:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_map_east_map_map_north_map_map_south_map_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='height',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(1000)], verbose_name='맵 높이'),
        ),
        migrations.AddField(
            model_name='map',
            name='width',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(1000)], verbose_name='맵 너비'),
        ),
        migrations.AlterField(
            model_name='map',
            name='coordinate',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='좌표'),
        ),
        migrations.AlterField(
            model_name='map',
            name='east_map',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='east_map_of', to='system.map', verbose_name='동쪽으로 향하는 맵'),
        ),
        migrations.AlterField(
            model_name='map',
            name='north_map',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='north_map_of', to='system.map', verbose_name='북쪽으로 향하는 맵'),
        ),
        migrations.AlterField(
            model_name='map',
            name='south_map',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='south_map_of', to='system.map', verbose_name='남쪽으로 향하는 맵'),
        ),
        migrations.AlterField(
            model_name='map',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='west_map',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='west_map_of', to='system.map', verbose_name='서쪽으로 향하는 맵'),
        ),
    ]
