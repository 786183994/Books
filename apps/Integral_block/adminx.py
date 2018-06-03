# _*_ coding: utf-8 _*_
__auther__ = '刘凌晨'
__date__ = '2018/5/29 17:28'

import xadmin
from .models import Integral, Grade


class IntegralAdmin(object):
    list_display = ['integral_numbers','add_time']
    list_filter = ['integral_numbers']#搜索的时候不对时间进行操作
    search_fields = ['integral_numbers','add_time']


class GradeAdmin(object):
    list_display = ['grade_classification','add_time']
    list_filter = ['grade_classification']#搜索的时候不对时间进行操作
    search_fields = ['grade_classification','add_time']


xadmin.site.register(Integral, IntegralAdmin)
xadmin.site.register(Grade, GradeAdmin)