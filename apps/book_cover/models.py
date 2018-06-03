# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

from users.models import UserProfile


class Books(models.Model):
    """
    图书
    """
    date = datetime.now().strftime("%y%m")
    user = models.ForeignKey(UserProfile, verbose_name=u"作者", null=True, blank=True)
    book_title = models.CharField(max_length=15, verbose_name=u"书名")
    book_volume = models.IntegerField(default=1, verbose_name=u"第几册")
    book_introduction = models.CharField(max_length=200, verbose_name=u"书介绍")
    book_page = models.IntegerField(default=30, verbose_name=u"总页数")
    book_actual_page = models.IntegerField(default=0, verbose_name=u"现有页数")
    collection = models.IntegerField(default=0, verbose_name=u"收藏量")
    collection_whether = models.CharField(max_length=20, verbose_name=u"是否收藏", default="收藏")
    book_number = models.CharField(null=True, blank=True, max_length=15, default="ZC"+date+"99Y", verbose_name=u"书籍编号")
    fav_point = models.IntegerField(default=0, verbose_name=u"点赞量")
    fav_whether = models.CharField(max_length=20, verbose_name=u"是否点赞", default="点赞")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"图书"
        verbose_name_plural = verbose_name

    def get_nums(self):
        return self.book_actual_page*100/self.book_page

    def __unicode__(self):
        return self.book_title


class PublicTable(models.Model):
    """
    众筹表
    """
    CROWD = (
        ("unfinished", u"众筹中"),
        ("end", u"众筹结束"),
    )
    books = models.ForeignKey(Books, verbose_name=u"书籍")
    public_price = models.IntegerField(default=50, verbose_name=u"众筹价格")
    book_state = models.CharField(max_length=20, choices=CROWD,default="unfinished", null=True, blank=True, verbose_name=u"众筹状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"众筹"
        verbose_name_plural = verbose_name


class BookCollCard(models.Model):
    """
    藏书证
    """
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    book_collection_card = models.CharField(max_length=15, verbose_name=u"藏书证编号", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"藏书证"
        verbose_name_plural = verbose_name