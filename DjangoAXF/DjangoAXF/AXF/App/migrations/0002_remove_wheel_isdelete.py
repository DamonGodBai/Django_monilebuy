# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-05 03:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wheel',
            name='isDelete',
        ),
    ]
