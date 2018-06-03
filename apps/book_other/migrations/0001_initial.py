# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-29 16:45
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_content', models.CharField(max_length=500, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_thumbs_up', models.IntegerField(default=0, verbose_name='\u70b9\u8d5e\u6570')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bdd\u9898',
                'verbose_name_plural': '\u8bdd\u9898',
            },
        ),
        migrations.CreateModel(
            name='FixedFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explain', models.CharField(max_length=200, verbose_name='\u85cf\u4e66\u8bc1\u8bf4\u660e')),
                ('brief_introduction', DjangoUeditor.models.UEditorField(default='', verbose_name='\u516c\u53f8\u7b80\u4ecb')),
                ('company_name', models.CharField(max_length=30, verbose_name='\u516c\u53f8\u540d\u79f0')),
                ('autograph', models.CharField(max_length=100, verbose_name='\u4f17\u7b79\u7b7e\u540d')),
                ('pay_notice', models.CharField(max_length=1000, verbose_name='\u4ed8\u8d39\u987b\u77e5')),
            ],
            options={
                'verbose_name': '\u56fa\u5b9a\u64cd\u4f5c',
                'verbose_name_plural': '\u56fa\u5b9a\u64cd\u4f5c',
            },
        ),
        migrations.CreateModel(
            name='RelationShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_payment', models.CharField(choices=[('paid', '\u5df2\u4ed8\u6b3e'), ('unpaid', '\u672a\u4ed8\u6b3e')], max_length=30, verbose_name='\u662f\u5426\u4ed8\u6b3e')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4ed8\u6b3e\u660e\u7ec6',
                'verbose_name_plural': '\u4ed8\u6b3e\u660e\u7ec6',
            },
        ),
        migrations.CreateModel(
            name='UserClick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='\u6570\u636eid')),
                ('fav_type', models.IntegerField(choices=[(1, '\u4f17\u7b79'), (2, '\u8bf4\u8bf4')], default=1, verbose_name='\u70b9\u8d5e\u7c7b\u578b')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u70b9\u8d5e',
                'verbose_name_plural': '\u7528\u6237\u70b9\u8d5e',
            },
        ),
        migrations.CreateModel(
            name='UserCooperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooperation_name', models.CharField(max_length=30, verbose_name='\u5408\u4f5c\u8005')),
                ('cooperation_email', models.CharField(max_length=50, verbose_name='\u5408\u4f5c\u8005\u90ae\u7bb1')),
                ('cooperation_tel', models.CharField(max_length=11, verbose_name='\u5408\u4f5c\u8005\u7535\u8bdd')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5408\u4f5c\u5546',
                'verbose_name_plural': '\u5408\u4f5c\u5546',
            },
        ),
        migrations.CreateModel(
            name='UserFavotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='\u6570\u636eid')),
                ('fav_type', models.IntegerField(choices=[(1, '\u4f17\u7b79'), (2, '\u8bf4\u8bf4')], default=1, verbose_name='\u6536\u85cf\u7c7b\u578b')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6536\u85cf',
                'verbose_name_plural': '\u7528\u6237\u6536\u85cf',
            },
        ),
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='\u6570\u636eid')),
                ('fav_type', models.IntegerField(choices=[(1, '\u4f17\u7b79'), (2, '\u8bf4\u8bf4')], default=1, verbose_name='\u70b9\u8d5e\u7c7b\u578b')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u5173\u6ce8',
                'verbose_name_plural': '\u7528\u6237\u5173\u6ce8',
            },
        ),
    ]