# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20170320_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=12, unique=True)),
                ('course_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SectorSkillCouncil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_skill_council_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='jobrole',
            name='job_role_sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SectorSkillCouncil'),
        ),
        migrations.AddField(
            model_name='courseinfo',
            name='course_job_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.JobRole'),
        ),
    ]