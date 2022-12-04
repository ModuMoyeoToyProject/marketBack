# Generated by Django 4.0 on 2022-12-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventoryID', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('weight', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlayerCharacter',
            fields=[
                ('playerID', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('statusID', models.CharField(max_length=45)),
                ('jobID', models.CharField(max_length=45)),
                ('inventoryID', models.CharField(max_length=45)),
                ('level', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('title', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('statusID', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('Hp', models.IntegerField()),
                ('Mp', models.IntegerField()),
                ('Str', models.IntegerField()),
                ('Dex', models.IntegerField()),
                ('Con', models.IntegerField()),
                ('Attk', models.IntegerField()),
                ('Def', models.IntegerField()),
                ('Hit', models.IntegerField()),
                ('Dodge', models.IntegerField()),
                ('Block', models.IntegerField()),
                ('Critical', models.IntegerField()),
                ('Agility', models.IntegerField()),
                ('Speed', models.IntegerField()),
                ('Friendly', models.IntegerField()),
                ('buffID', models.IntegerField()),
                ('debuffID', models.IntegerField()),
            ],
        ),
    ]