# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restshop', '0021_auto_20170904_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitimage',
            name='image',
            field=models.ImageField(upload_to='media/product_images/'),
        ),
    ]
