# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 18:39
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_update-meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdistributionsitedetails',
            name='zip_codes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), null=True, size=None),
        ),
    ]
