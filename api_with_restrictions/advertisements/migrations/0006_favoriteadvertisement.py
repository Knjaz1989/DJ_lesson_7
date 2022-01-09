# Generated by Django 4.0.1 on 2022-01-08 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0005_alter_advertisement_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteAdvertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='advertisements.advertisement')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
