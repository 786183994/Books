# _*_ coding: utf-8 _*_
__auther__ = '刘凌晨'
__date__ = '2018/4/25 0:41'

import xadmin

from .models import EditAddDetails, BookDetails


class EditAddDetailsAdmin(object):
    list_display  = ['title','content']
    list_filter = ['title','content']#搜索的时候不对时间进行操作
    search_fields = ['title','content']

class BookDetailsAdmin(object):
    list_display  = ['title','content']
    list_filter = ['title','content']#搜索的时候不对时间进行操作
    search_fields = ['title','content']


xadmin.site.register(EditAddDetails,EditAddDetailsAdmin);
xadmin.site.register(BookDetails,BookDetailsAdmin);