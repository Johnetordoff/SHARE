# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-17 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0014_auto_20170112_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractcreativework',
            name='justification',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='abstractcreativework',
            name='registration_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='abstractcreativework',
            name='withdrawn',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='abstractcreativeworkversion',
            name='justification',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='abstractcreativeworkversion',
            name='registration_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='abstractcreativeworkversion',
            name='withdrawn',
            field=models.NullBooleanField(default=False),
        ),
    ]
