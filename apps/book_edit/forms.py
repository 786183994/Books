# _*_ coding: utf-8 _*_
__auther__ = '刘凌晨'
__date__ = '2018/5/24 17:49'

from django import forms


class EditForm(forms.Form):
    """
        判断是否在说说中写入内容
    """
    #标题
    title = forms.CharField(required=True, max_length=50)#表示为必填字段
    #主内容
    text = forms.CharField(required=True, max_length=300)