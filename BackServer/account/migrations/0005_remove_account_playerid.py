# Generated by Django 4.0 on 2022-12-05 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_id_alter_account_playerid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='playerID',
        ),
    ]
