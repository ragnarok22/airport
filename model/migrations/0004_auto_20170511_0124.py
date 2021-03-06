# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import model.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_area'),
        ('model', '0003_lawrequirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawrequirements',
            name='file',
            field=models.FileField(blank=True, upload_to=model.models.url, verbose_name='Fichero'),
        ),
        migrations.AddField(
            model_name='lawrequirements',
            name='pub_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de publicación'),
        ),
        migrations.AddField(
            model_name='lawrequirements',
            name='register_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Profile', verbose_name='Registrado por'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lawrequirements',
            name='environmental_aspects',
            field=models.TextField(verbose_name='Aspectos ambientales'),
        ),
        migrations.AlterField(
            model_name='lawrequirements',
            name='law',
            field=models.CharField(max_length=50, verbose_name='Ley'),
        ),
        migrations.AlterField(
            model_name='lawrequirements',
            name='requirements',
            field=models.TextField(verbose_name='Requerimientos'),
        ),
        migrations.AlterField(
            model_name='lawrequirements',
            name='section',
            field=models.CharField(max_length=100, verbose_name='Sección'),
        ),
    ]
