# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_remove_studentcourseregistration_scr_training_center_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourseregistration',
            name='scr_training_center_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.TrainingCenter'),
        ),
    ]
