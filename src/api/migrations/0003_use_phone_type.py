# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_request_attributes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='home_phone',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='request',
            name='mobile_phone',
        ),
        migrations.AddField(
            model_name='request',
            name='phone_type',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
