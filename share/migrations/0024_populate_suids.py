# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-15 02:48
from __future__ import unicode_literals

from django.db import migrations
from django.core import management


def load_sources(apps, schema_editor):
    management.call_command('loadsources', apps=apps)


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0023_auto_20170315_0241'),
    ]

    operations = [
        # Populate Source, SourceConfig, SourceIcon, Transformer, Harvester
        migrations.RunPython(load_sources),

        # Create SUIDs for all existing rawdatum
        migrations.RunSQL('''
            INSERT INTO share_sourceuniqueidentifier (identifier, source_config_id)
            SELECT DISTINCT raw.provider_doc_id, config.id
            FROM share_rawdatum raw
            JOIN share_sourceconfig config ON raw.app_label = config.label;

            UPDATE share_rawdatum raw SET suid_id = (
                SELECT suid.id FROM share_sourceuniqueidentifier suid
                JOIN share_sourceconfig config ON suid.source_config_id = config.id
                WHERE raw.provider_doc_id = suid.identifier AND raw.app_label = config.label
            );
        '''),
    ]
