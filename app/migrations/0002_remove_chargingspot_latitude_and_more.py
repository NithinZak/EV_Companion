# Generated by Django 5.0.1 on 2024-02-04 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chargingspot',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='chargingspot',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='chargingspot',
            name='station',
        ),
    ]
