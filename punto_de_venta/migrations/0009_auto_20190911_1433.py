# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-11 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punto_de_venta', '0008_auto_20190911_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja_operacion',
            name='fecha_cierre',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
