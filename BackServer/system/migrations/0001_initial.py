# Generated by Django 4.1.1 on 2023-01-04 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bgm',
            fields=[
                ('bgmID', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('bgmName', models.CharField(max_length=45)),
                ('bgmType', models.CharField(max_length=45)),
                ('bgmPath', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('dateID', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('dateEffect', models.CharField(max_length=45)),
                ('darkModeYn', models.CharField(max_length=45)),
                ('holidayYn', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='이름')),
                ('description', models.CharField(blank=True, max_length=64, verbose_name='설명')),
                ('required_level', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='진입 요구 레벨 (1~100)')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('coordinate', models.CharField(max_length=255, verbose_name='좌표')),
                ('street', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '맵',
                'verbose_name_plural': '맵',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('sysID', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('dateID', models.CharField(max_length=45)),
                ('weatherID', models.CharField(max_length=45)),
                ('timerID', models.CharField(max_length=45)),
                ('bgmID', models.CharField(max_length=45)),
                ('mapID', models.CharField(max_length=45)),
                ('auth', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('timerID', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('timerName', models.CharField(max_length=45)),
                ('timerType', models.CharField(max_length=45)),
                ('timerSec', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('weatherID', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('weatherName', models.CharField(max_length=45)),
                ('weatherType', models.CharField(max_length=45)),
                ('weatherEffect', models.CharField(max_length=45)),
            ],
        ),
    ]
