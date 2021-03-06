# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-03 18:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_other', '0005_auto_20180529_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignInFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_in', models.IntegerField(choices=[(0, '\u7b7e\u5230'), (1, '\u5df2\u7b7e\u5230')], default=0, verbose_name='\u7b7e\u5230\u7c7b\u578b')),
                ('sign_in_end', models.IntegerField(default=0, verbose_name='\u7b7e\u5230')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7b7e\u5230',
                'verbose_name_plural': '\u7528\u6237\u7b7e\u5230',
            },
        ),
    ]
