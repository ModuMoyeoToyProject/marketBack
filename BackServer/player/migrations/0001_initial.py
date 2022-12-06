# Generated by Django 4.0 on 2022-12-05 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0005_remove_account_playerid'),
    ]

    operations = [
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
        migrations.CreateModel(
            name='PlayerCharacter',
            fields=[
                ('playerID', models.AutoField(primary_key=True, serialize=False)),
                ('statusID', models.CharField(max_length=45)),
                ('jobID', models.CharField(max_length=45, null=True)),
                ('level', models.IntegerField(default=1)),
                ('exp', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=45, null=True)),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventoryID', models.AutoField(primary_key=True, serialize=False)),
                ('weight', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('PlayerCharacter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.playercharacter')),
            ],
        ),
    ]
