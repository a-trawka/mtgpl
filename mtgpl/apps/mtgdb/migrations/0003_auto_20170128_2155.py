# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtgdb', '0002_expansion_border'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last name'),
        ),
    ]