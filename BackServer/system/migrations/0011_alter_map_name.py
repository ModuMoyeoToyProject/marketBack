# Generated by Django 4.1.1 on 2023-01-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_alter_map_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='name',
            field=models.CharField(default='fdsa', max_length=32, unique=True, verbose_name='이름'),
            preserve_default=False,
        ),
    ]
