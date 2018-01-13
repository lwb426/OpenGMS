# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-13 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180113_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_by', to=settings.AUTH_USER_MODEL),
        ),
    ]