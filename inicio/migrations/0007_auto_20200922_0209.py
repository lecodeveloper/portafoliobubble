# Generated by Django 3.0.8 on 2020-09-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_auto_20200922_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas_de_contacto',
            name='tel',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]