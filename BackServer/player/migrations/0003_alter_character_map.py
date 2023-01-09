# Generated by Django 4.1.1 on 2023-01-09 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_alter_map_name'),
        ('player', '0002_remove_character_location_character_map_character_x_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='map',
            field=models.ForeignKey(default='중앙 광장', null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.map', to_field='name', verbose_name='현재 맵'),
        ),
    ]
