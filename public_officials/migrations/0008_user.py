# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-05-30 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_officials', '0007_auto_20170530_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legislators', models.ManyToManyField(to='public_officials.Legislator')),
            ],
        ),
    ]