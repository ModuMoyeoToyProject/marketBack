# Generated by Django 4.0 on 2022-12-28 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_remove_dialogue_type_dialogue_maincategory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dialogue',
            old_name='middleCateogry',
            new_name='middleCateogory',
        ),
        migrations.RenameField(
            model_name='dialogue',
            old_name='subCateogry',
            new_name='subCateogory',
        ),
    ]
