# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


#user功能表：进行表字段的设置
class UserProfile(AbstractUser):
    """
    登录用户信息存储
    """
    SEX = (
        ("male", u"男"),
        ("female", u"女"),
    )
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=7, choices=SEX,default="female", verbose_name=u"性别")
    address = models.CharField(max_length=100, verbose_name=u"地址", default="")
    mobile = models.CharField(max_length=11,verbose_name=u"手机号", null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/touxiang.png", max_length=100)
    identity_id = models.CharField(max_length=18, verbose_name=u"身份证号")
    author_number = models.CharField(max_length=15, verbose_name=u"作者编号", null=True, blank=True)
    signature = models.CharField(max_length=200, verbose_name=u"个性签名", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):#邮箱验证
    OPERATION = (
        ("register", "注册"),
        ("forget", "找回密码"),
        ("update_email", u"修改邮箱"),
    )
    code = models.CharField(max_length=20, verbose_name=u"验证码");
    email = models.EmailField(max_length=20, verbose_name=u"邮箱");
    send_type = models.CharField(verbose_name="验证码类型", choices=OPERATION, max_length=30)
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now);

    class Meta:
        verbose_name = u"邮箱验证码";
        verbose_name_plural = verbose_name;

    #此处重载unicode方法，直接体现在页面显示上
    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):#轮播图
    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%M", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200,verbose_name=u"访问地址")
    index = models.IntegerField(default=1,verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name