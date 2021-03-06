# Generated by Django 4.0.1 on 2022-01-06 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0004_remove_advertisement_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.TextField(choices=[('OPEN', 'Открыто'), ('CLOSED', 'Закрыто'), ('DRAFT', 'Черновик')], default='OPEN'),
        ),
    ]
