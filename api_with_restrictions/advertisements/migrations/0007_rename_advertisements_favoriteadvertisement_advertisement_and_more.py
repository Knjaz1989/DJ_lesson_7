# Generated by Django 4.0.1 on 2022-01-08 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0006_favoriteadvertisement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoriteadvertisement',
            old_name='advertisements',
            new_name='advertisement',
        ),
        migrations.RenameField(
            model_name='favoriteadvertisement',
            old_name='users',
            new_name='user',
        ),
    ]
