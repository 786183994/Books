# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from book_cover.models import Books
from users.models import UserProfile
# Create your models here.


#说说详情页面
class EditAddDetails(models.Model):

    user = models.ForeignKey(UserProfile, verbose_name=u"用户", null=True, blank=True)
    title = models.CharField(max_length=20, verbose_name=u"名称")
    content = models.CharField(max_length=500, verbose_name=u"内容")
    background_pic = models.ImageField(upload_to="background/%Y/%m",verbose_name=u"背景图",max_length=100)
    fav_point = models.IntegerField(default=0, verbose_name=u"点赞量")
    fav_whether = models.CharField(max_length=20, verbose_name=u"是否点赞", default="点赞")
    follow_whether = models.CharField(max_length=20, verbose_name=u"是否关注", default="关注")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"编辑与详情"
        verbose_name_plural = verbose_name

    def get_content(self):
        return self.content[:10]+"...."


#众筹详情编辑页面
class BookDetails(models.Model):
    book = models.ForeignKey(Books, verbose_name=u"书籍")
    title = models.CharField(max_length=20, verbose_name=u"名称")
    content = models.CharField(max_length=500, verbose_name=u"内容")
    background_pic = models.ImageField(upload_to="background/%Y/%m",verbose_name=u"背景图",max_length=100)
    fav_point = models.IntegerField(default=0, verbose_name=u"点赞量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"众筹详情编辑"
        verbose_name_plural = verbose_name

    def get_content(self):
        return self.content[:10]+"...."