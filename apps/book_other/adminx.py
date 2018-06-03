# _*_ coding: utf-8 _*_
__auther__ = '刘凌晨'
__date__ = '2018/4/25 0:11'

import xadmin

from .models import Conversation,Comment, FixedFormat, UserClick, UserCooperation, RelationShip


class ConversationAdmin(object):
    list_display = ['con_user', 'add_time','con_thumbs_up']  # 表示在页面中显示时，出现的内容标题
    search_fields = ['con_user__name','con_thumbs_up']  # 搜索框功能，数组里面的数据表示的是可以进行搜索的类型
    list_filter = ['con_user', 'add_time','con_thumbs_up']  # 过滤器


class CommentAdmin(object):
    list_display  = ['com_user','com_content','add_time']
    list_filter = ['com_user__username','com_content']#搜索的时候不对时间进行操作
    search_fields = ['com_user','com_content','add_time']


class FixedFormatAdmin(object):
    list_display  = ['explain','company_name','autograph']
    list_filter = ['explain','company_name','autograph']#搜索的时候不对时间进行操作
    search_fields = ['explain','company_name','autograph']


class UserClickAdmin(object):
    list_display = ['fav_type']
    list_filter = ['fav_type']#搜索的时候不对时间进行操作
    search_fields = ['fav_type']


class UserCooperationAdmin(object):
    list_display  = ['cooperation_name','cooperation_tel']
    list_filter = ['cooperation_name','cooperation_tel']#搜索的时候不对时间进行操作
    search_fields = ['cooperation_name','cooperation_tel']


class RelationShipAdmin(object):
    list_display  = ['is_payment','add_time']
    list_filter = ['is_payment']#搜索的时候不对时间进行操作
    search_fields = ['is_payment','add_time']


xadmin.site.register(RelationShip,RelationShipAdmin)
xadmin.site.register(UserCooperation,UserCooperationAdmin)
xadmin.site.register(UserClick,UserClickAdmin);
xadmin.site.register(FixedFormat,FixedFormatAdmin);
xadmin.site.register(Conversation,ConversationAdmin);
xadmin.site.register(Comment,CommentAdmin);