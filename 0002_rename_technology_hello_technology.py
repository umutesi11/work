# Generated by Django 4.0.5 on 2022-06-14 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hello',
            old_name='Technology',
            new_name='technology',
        ),
    ]
