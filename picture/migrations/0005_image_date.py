# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0004_auto_20170509_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
