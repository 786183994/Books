# _*_ coding: utf-8 _*_
__auther__ = '刘凌晨'
__date__ = '2018/4/25 0:53'

import xadmin

from .models import Books, PublicTable, BookCollCard


class BooksAdmin(object):
    list_display = ['book_title','book_volume','book_introduction']
    list_filter = ['book_title','book_volume','book_introduction']#搜索的时候不对时间进行操作
    search_fields = ['book_title','book_volume','book_introduction']


class PublicTableAdmin(object):
    list_display  = ['public_price']
    list_filter = ['public_price']#搜索的时候不对时间进行操作
    search_fields = ['public_price']


class BookCollCardAdmin(object):
    list_display = ['book_collection_card','add_time']
    list_filter = ['book_collection_card']#搜索的时候不对时间进行操作
    search_fields = ['book_collection_card','add_time']


xadmin.site.register(BookCollCard,BookCollCardAdmin)
xadmin.site.register(Books,BooksAdmin)
xadmin.site.register(PublicTable,PublicTableAdmin)