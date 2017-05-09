# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import model.models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelr01pg01',
            name='pub_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='modelr01pg01',
            name='year',
            field=models.IntegerField(validators=[model.models.validate_year], verbose_name='Año'),
        ),
    ]
