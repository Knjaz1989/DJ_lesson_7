# Generated by Django 4.0.1 on 2022-01-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_alter_advertisement_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]