# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0002_auto_20170515_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generalprogramaudit',
            options={'verbose_name': 'Programa General', 'verbose_name_plural': 'Programas Generales'},
        ),
    ]
