# Generated by Django 3.2.16 on 2023-02-07 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_recipe_recipie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipie',
            new_name='Recipe',
        ),
    ]
