# Generated by Django 4.1.1 on 2023-01-02 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_fish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteminfo',
            name='count',
        ),
    ]