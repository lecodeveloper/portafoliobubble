# Generated by Django 3.0.8 on 2020-09-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_auto_20200922_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas_de_contacto',
            name='tel',
            field=models.BigIntegerField(blank=True, default=0),
        ),
    ]
