# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import model.models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0010_communication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='adopted_decision',
            field=models.CharField(max_length=200, verbose_name='Decision adoptada'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='airport_name',
            field=models.CharField(max_length=100, verbose_name='Nombre del aereopuerto'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Area', verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='contact_data',
            field=models.TextField(verbose_name='Datos del contacto'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='distribution_date',
            field=models.DateField(verbose_name='Fecha de distribucion'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='emission_path',
            field=models.CharField(max_length=200, verbose_name='Via de emision'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='info_content',
            field=models.TextField(verbose_name='Contenido del la informacion'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='reception_way',
            field=models.CharField(max_length=200, verbose_name='Via de recepcion'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='register_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile', verbose_name='Registrado por'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='type_communication',
            field=models.CharField(choices=[('i', 'interna'), ('e', 'externa')], max_length=1, verbose_name='Tipo de comunicacion'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='year',
            field=models.IntegerField(validators=[model.models.validate_year], verbose_name='Año'),
        ),
    ]
