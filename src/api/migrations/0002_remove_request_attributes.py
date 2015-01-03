# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='city',
        ),
        migrations.RemoveField(
            model_name='request',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='request',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='request',
            name='state',
        ),
        migrations.AddField(
            model_name='request',
            name='name',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
    ]
