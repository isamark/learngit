# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsinfo',
            old_name='ghnit',
            new_name='gunit',
        ),
    ]
