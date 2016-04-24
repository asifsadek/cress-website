# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0007_auto_20160424_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='cycle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='action', to='box.Cycle'),
            preserve_default=False,
        ),
    ]
