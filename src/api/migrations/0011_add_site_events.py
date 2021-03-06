# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 16:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_add_phone2'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistributionSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventDistributionSiteDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('max_requests', models.IntegerField(null=True)),
                ('distribution_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DistributionSite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('active', models.BooleanField()),
                ('distribution_sites', models.ManyToManyField(through='api.EventDistributionSiteDetails', to='api.DistributionSite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='EventDistributionSiteDetails',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Event'),
        ),
    ]
