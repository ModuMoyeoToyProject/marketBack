# Generated by Django 4.0 on 2022-12-28 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_rename_middlecateogry_dialogue_middlecateogory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dialogue',
            old_name='middleCateogory',
            new_name='middleCategory',
        ),
        migrations.RenameField(
            model_name='dialogue',
            old_name='subCateogory',
            new_name='subCategory',
        ),
    ]