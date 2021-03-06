# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_batchinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='user_registration_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidateregistration',
            name='c_app_user_email',
            field=models.CharField(default=False, max_length=255),
            preserve_default=False,
        ),
    ]
