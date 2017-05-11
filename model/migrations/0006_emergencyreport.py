# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_auto_20170511_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(unique=True)),
                ('report', models.CharField(choices=[('e', 'Situacion de emergencia'), ('a', 'Accidente'), ('r', 'Real'), ('s', 'Simulacro o Ejercicio')], default='s', max_length=1)),
                ('datetime', models.DateTimeField()),
                ('place', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]