# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-16 22:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='timeGap',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(24)]),
        ),
    ]
