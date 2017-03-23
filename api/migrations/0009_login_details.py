# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_login_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=255, unique=True)),
                ('user_password', models.CharField(max_length=128)),
                ('user_last_login', models.DateTimeField(blank=True, null=True)),
                ('user_date_joined', models.DateTimeField()),
                ('user_name', models.CharField(max_length=70)),
            ],
        ),
    ]
