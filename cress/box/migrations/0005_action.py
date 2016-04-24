# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0004_auto_20160424_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('action_type', models.CharField(choices=[('UV light', 'UV light'), ('Water', 'Water')], max_length=100)),
                ('decision', models.IntegerField()),
                ('start_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
            },
        ),
    ]
