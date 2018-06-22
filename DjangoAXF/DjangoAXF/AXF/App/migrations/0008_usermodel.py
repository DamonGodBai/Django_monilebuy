# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('icon', models.ImageField(upload_to='')),
                ('sex', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]