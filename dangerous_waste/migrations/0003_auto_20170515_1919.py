# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dangerous_waste', '0002_auto_20170515_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dangerouswaste',
            name='wastes',
        ),
        migrations.AddField(
            model_name='waste',
            name='dangerous_waste',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dangerous_waste.DangerousWaste'),
            preserve_default=False,
        ),
    ]