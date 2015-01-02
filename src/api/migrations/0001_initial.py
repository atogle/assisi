# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, null=True, blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=200, null=True, blank=True)),
                ('state', models.CharField(max_length=200, null=True, blank=True)),
                ('zip', models.CharField(max_length=200, null=True, blank=True)),
                ('email', models.CharField(max_length=200, null=True, blank=True)),
                ('home_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('mobile_phone', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
