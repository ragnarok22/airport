# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20170518_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='nationalpassengerpoll',
            name='airline',
            field=models.CharField(default='Jose Marti', max_length=150, verbose_name='Terminal aerea'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nationalpassengerpoll',
            name='date',
            field=models.DateField(default='2017-10-15', verbose_name='Fecha'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nationalpassengerpoll',
            name='no_fly',
            field=models.PositiveIntegerField(default=20171015, verbose_name='Numero de Vuelo'),
            preserve_default=False,
        ),
    ]
