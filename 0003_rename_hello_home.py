# Generated by Django 4.0.5 on 2022-06-14 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_rename_technology_hello_technology'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hello',
            new_name='Home',
        ),
    ]
