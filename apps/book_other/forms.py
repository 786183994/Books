# _*_ coding: utf-8 _*_
__auther__ = '刘凌晨'
__date__ = '2018/4/27 13:24'

from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(required=True)