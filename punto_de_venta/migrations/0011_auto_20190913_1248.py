# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-13 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import punto_de_venta.validators


class Migration(migrations.Migration):

    dependencies = [
        ('punto_de_venta', '0010_ubicacion_codigo_postal'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='caja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='punto_de_venta.Cajas'),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='no_ext',
            field=models.CharField(max_length=10, validators=[punto_de_venta.validators.validate_digit]),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='no_int',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[punto_de_venta.validators.validate_digit]),
        ),
    ]
