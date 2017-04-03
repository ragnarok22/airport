# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('title', models.CharField(max_length=100, verbose_name='titulo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripcion')),
            ],
        ),
    ]
