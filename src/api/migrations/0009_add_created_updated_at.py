# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_request_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now(), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now(), auto_now=True),
            preserve_default=False,
        ),
    ]
