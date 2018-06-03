# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-29 16:48
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integral_numbers', models.CharField(choices=[('intermediate', '\u4e2d\u7ea7\u4f1a\u5458'), ('civilian', '\u5e73\u6c11'), ('senior', '\u9ad8\u7ea7\u4f1a\u5458'), ('ordinary', '\u666e\u901a\u4f1a\u5458')], max_length=10, verbose_name='\u7b49\u7ea7\u5206\u7c7b')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u7b49\u7ea7',
                'verbose_name_plural': '\u7b49\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='Integral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integral_numbers', models.CharField(max_length=10, verbose_name='\u603b\u79ef\u5206')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u79ef\u5206\u64cd\u4f5c',
                'verbose_name_plural': '\u79ef\u5206\u64cd\u4f5c',
            },
        ),
    ]