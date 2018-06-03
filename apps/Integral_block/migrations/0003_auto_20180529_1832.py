# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-29 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Integral_block', '0002_auto_20180529_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade_classification',
            field=models.CharField(choices=[('intermediate', '\u4e2d\u7ea7\u4f1a\u5458'), ('civilian', '\u5e73\u6c11'), ('senior', '\u9ad8\u7ea7\u4f1a\u5458'), ('ordinary', '\u666e\u901a\u4f1a\u5458')], default='civilian', max_length=10, verbose_name='\u7b49\u7ea7\u5206\u7c7b'),
        ),
        migrations.AlterField(
            model_name='integral',
            name='integral_numbers',
            field=models.IntegerField(default=0, max_length=10, verbose_name='\u603b\u79ef\u5206'),
        ),
    ]