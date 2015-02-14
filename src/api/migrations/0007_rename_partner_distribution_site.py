# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_request_partner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='partner',
            new_name='distribution_site',
        ),
    ]
