# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagement', '0002_auto_20170307_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
