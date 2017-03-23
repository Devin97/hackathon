# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_testtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'custom_test',
                'managed': True,
            },
        ),
    ]