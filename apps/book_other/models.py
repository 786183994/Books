# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

from users.models import UserProfile
from book_edit.models import EditAddDetails
from book_cover.models import Books
# Create your models here.


class Conversation(models.Model):
    """
    话题表
    """
    con_edit = models.ForeignKey(EditAddDetails, verbose_name=u"说说")
    con_user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    con_thumbs_up = models.IntegerField(default=0,verbose_name=u"点赞数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"话题"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """
    评论表
    """
    com_user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    con_edit = models.ForeignKey(EditAddDetails, verbose_name=u"说说")
    com_content = models.CharField(max_length=500, verbose_name=u"评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = verbose_name


class UserFavotion(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(choices=((1, "众筹"),(2, "说说")), default=1, verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserClick(models.Model):
    """
    用户点赞
    """
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(choices=((1, "众筹"), (2, "说说")), default=1, verbose_name=u"点赞类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户点赞"
        verbose_name_plural = verbose_name


class UserFollow(models.Model):
    """
    用户关注
    """
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(choices=((1, "众筹"), (2, "说说")), default=1, verbose_name=u"点赞类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户关注"
        verbose_name_plural = verbose_name


class FixedFormat(models.Model):
    """
        固定操作
    """
    #我的藏书证
    explain = models.CharField(max_length=200, verbose_name=u"藏书证说明")
    #公司
    brief_introduction = UEditorField(u'公司简介', width=500, height=300, imagePath="company/image/", default="")#富文本编辑器
    company_name = models.CharField(max_length=30, verbose_name=u"公司名称")
    #众筹
    autograph = models.CharField(max_length=100, verbose_name=u"众筹签名")
    pay_notice = models.CharField(max_length=1000, verbose_name=u"付费须知")
    #权限
    increase_integral = models.CharField(max_length=1000, verbose_name=u"积分须知", null=True, blank=True)
    jurisdiction_explain = models.CharField(max_length=1000, verbose_name=u"权限说明", null=True, blank=True)

    class Meta:
        verbose_name = u"固定操作"
        verbose_name_plural = verbose_name


class UserCooperation(models.Model):
    """
    合作商
    """
    cooperation_name = models.CharField(max_length=30, verbose_name=u"合作者")
    cooperation_email = models.CharField(max_length=50, verbose_name=u"合作者邮箱")
    cooperation_tel = models.CharField(max_length=11, verbose_name=u"合作者电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"合作商"
        verbose_name_plural = verbose_name


class RelationShip(models.Model):
    """
        作者和书关系
    """
    PAYMENT = {
        ("paid", "已付款"),
        ("unpaid", "未付款")
    }
    book = models.ForeignKey(Books, verbose_name=u"书籍", null=True, blank=True)
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", null=True, blank=True)
    is_payment = models.CharField(max_length=30, verbose_name=u"是否付款", choices=PAYMENT, default="unpaid")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"付款明细"
        verbose_name_plural = verbose_name


class SignInFollow(models.Model):
    """
    用户签到
    """
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    sign_in = models.IntegerField(choices=((0, "签到"), (1, "已签到")), default=0, verbose_name=u"签到类型")
    sign_in_end = models.IntegerField(verbose_name=u"签到", default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户签到"
        verbose_name_plural = verbose_name