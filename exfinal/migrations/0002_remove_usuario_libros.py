# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exfinal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='Libros',
        ),
    ]
