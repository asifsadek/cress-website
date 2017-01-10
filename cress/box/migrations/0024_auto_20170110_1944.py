# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 18:44
from __future__ import unicode_literals

import box.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0023_auto_20161222_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(max_length=254, upload_to=box.models.image_directory),
        ),
    ]
