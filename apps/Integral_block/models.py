# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from users.models import UserProfile
# Create your models here.


class Integral(models.Model):
    """
        积分表
                签到 2-5的随机积分
                邀请 +50
                发表页面 +60
                发表话题 0-6 最高送四次
                话题精选 +10 点赞量超过88
                藏书正认证 2400 规定出来了。
    """
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    integral_numbers = models.IntegerField(max_length=100000, verbose_name=u"总积分", default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"积分操作"
        verbose_name_plural = verbose_name


class Grade(models.Model):
    """
        等级表
            等级表设定为只可以超级用户进行操作
    """
    Grade = {
        ("civilian", "平民"),
        ("ordinary", "普通会员"),
        ("intermediate", "中级会员"),
        ("senior", "高级会员")
    }
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    grade_classification = models.CharField(max_length=10,choices=Grade, verbose_name=u"等级分类", default="civilian")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"等级"
        verbose_name_plural = verbose_name