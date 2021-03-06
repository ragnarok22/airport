# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirLineRepresentPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InternationalPassengerPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.TextField(verbose_name='Su opinion')),
            ],
        ),
        migrations.CreateModel(
            name='InternationalService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Servicio')),
                ('evaluation', models.IntegerField(choices=[(0, 'No utilizado'), (1, 'Malo'), (2, 'Insatisfactorio'), (3, 'Bueno'), (4, 'Muy Bueno'), (5, 'Excelente')], verbose_name='Evaluacion')),
                ('why', models.TextField(blank=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.InternationalPassengerPoll', verbose_name='Encuesta a Pasajeros Internacionales')),
            ],
        ),
        migrations.CreateModel(
            name='NationalPassengerPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.TextField(verbose_name='Su opinion')),
            ],
            options={
                'verbose_name_plural': 'Encuestas a Pasajeros Nacionales',
                'verbose_name': 'Encuesta a Pasajeros Nacionales',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Servicio')),
                ('evaluation', models.IntegerField(choices=[(0, 'No utilizado'), (1, 'Malo'), (2, 'Insatisfactorio'), (3, 'Bueno'), (4, 'Muy Bueno'), (5, 'Excelente')], verbose_name='Evaluacion')),
                ('why', models.TextField(blank=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.NationalPassengerPoll', verbose_name='Encuesta a Pasajeros Nacionales')),
            ],
            options={
                'verbose_name_plural': 'Servicios',
                'verbose_name': 'Servicio',
            },
        ),
    ]
