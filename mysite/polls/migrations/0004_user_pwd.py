# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-09 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_pwd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
