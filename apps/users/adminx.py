# _*_ coding: utf-8 _*_
__auther__ = '刘凌晨'
__date__ = '2018/4/24 23:39'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner, UserProfile


# 开启主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


#修改页面显示功能
class GlobalSetting(object):
    site_title = "后台管理系统";#修改的是左上角的信息输出
    site_footer = "在线学习"#修改的是最下方的信息输出
    menu_style = "accordion"#收缩显示功能


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']#表示在页面中显示时，出现的内容标题
    search_fields = ['code','email','send_type']#搜索框功能，数组里面的数据表示的是可以进行搜索的类型
    list_filter = ['code','email','send_type','send_time']#过滤器
    model_icon = 'fa fa-envelope'

class BannerAdmin(object):
    list_display  = ['title','image','url','index','add_time']
    list_filter = ['title','image','url','index']#搜索的时候不对时间进行操作
    search_fields = ['title','image','url','index','add_time']
    model_icon = 'fa fa-group'

#将管理器与model进行注册关联
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin);
xadmin.site.register(Banner, BannerAdmin);
xadmin.site.register(views.BaseAdminView, BaseSetting);
xadmin.site.register(views.CommAdminView, GlobalSetting);