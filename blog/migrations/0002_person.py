# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-26 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[(b's', b'small'), (b'm', b'medium'), (b'l', b'large')], max_length=2)),
            ],
        ),
    ]