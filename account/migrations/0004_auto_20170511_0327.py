# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 03:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='sex',
            new_name='gender',
        ),
    ]
