# -*- coding: utf-8 -*-
"""Book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url,include
# from django.contrib import admin
from django.views.static import serve

from Book.settings import MEDIA_ROOT
from users.views import RegisterView, IndexView, LoginView, LogoutView, ActiveUserView, AddFavView, ClickFavView, UsersView, FollowFavView, PictureUploadView
from users.views import UserCangShuZhengView, UserShouCangPinView, UserOnTheCollectionPinView, UserOnThegOurView
from book_cover.views import ContactShowView, ContactShowListView, ContactBookShowView, ContactBookShowIdView, ContactShowListUnfinishedView
from book_edit.views import ContactListView, ContactWriteView, ContactMsgView, ContactNewestView, ContactSelectedView, ContactFollowView, EditSayView
from book_edit.views import ContactWriteHardcoverView, EditSayHardcoverView
from Integral_block.views import SignInView, JurisdictionView
# from book_other.views import ContactCommentView

urlpatterns = [
    url(r'^captcha/', include('captcha.urls')),

    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),#项目首页

    url(r'^sign_in$', SignInView.as_view(), name="sign_in"),  # 项目首页的签到
    url(r'^quanxian', JurisdictionView.as_view(), name="quanxian"),  # 进入权限页面

    url(r'^login/$', LoginView.as_view(), name="login"),#用户登陆
    url(r'^logout/$', LogoutView.as_view(), name="logout"),#退出登录状态
    url(r'^register/$',RegisterView.as_view(),name="register"),#用户注册
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"), # 用户邮箱激活

    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),  # 收藏
    url(r'^click_fav/$', ClickFavView.as_view(), name="click_fav"),  # 点赞
    url(r'^follow_fav/$', FollowFavView.as_view(), name="follow_fav"),  # 关注
    # url(r'^picture_upload/$', PictureUploadView.as_view(), name="picture_upload"),  # 图片上传

    url(r'contact_show/(?P<show_code>.*)/$', ContactShowView.as_view(), name="contact_show"),#众筹详情页面
    url(r'contact_list/$', ContactListView.as_view(), name="contact_list"),#说说列表页面
    url(r'contact_newest/$', ContactNewestView.as_view(), name="contact_newest"),  # 最新的说说页面
    url(r'contact_selected/$', ContactSelectedView.as_view(), name="contact_selected"),  # 精选的说说列表页面
    url(r'contact_follow/(?P<follow_code>.*)/$', ContactFollowView.as_view(), name="contact_follow"),  # 关注的说说列表页面

    url(r'contact_msg/(?P<msg_code>.*)/$', ContactMsgView.as_view(), name="contact_msg"),#话题详情页面
    url(r'contact_write/$', ContactWriteView.as_view(), name="contact_write"),#话题详情编辑页面
    url(r'edit_say/$', EditSayView.as_view(), name="edit_say"),  # 说说详情编辑页面
    url(r'contact_write_hardcover/$', ContactWriteHardcoverView.as_view(), name="contact_write_hardcover"),  # 发表众筹详情编辑页面
    url(r'edit_say_hardcover/$', EditSayHardcoverView.as_view(), name="edit_say_hardcover"),  # 说说详情编辑页面

    # url(r'contact_comment/(?P<comment_code>.*)/$', ContactCommentView.as_view(), name="contact_comment"),#说说详情评论页面
    url(r'users/$', UsersView.as_view(), name="users"),  # 我的主页面
    url(r'cangshuzheng/$', UserCangShuZhengView.as_view(), name="cangshuzheng"),  # 我的藏书证
    url(r'shoucangpin/$', UserShouCangPinView.as_view(), name="shoucangpin"),  # 我的收藏品
    url(r'onthecollectionpin/$', UserOnTheCollectionPinView.as_view(), name="onthecollectionpin"),  # 我的关于收藏品
    url(r'guanyuwomen/$', UserOnThegOurView.as_view(), name="guanyuwomen"),  # 我的关于收藏品

    url(r'^contact_show_list/(?P<msg_code>.*)$', ContactShowListView.as_view(), name="contact_show_list" ),#众筹精选(已完成)页面
    url(r'^contact_show_list_nofinish/(?P<msg_code>.*)$', ContactShowListUnfinishedView.as_view(), name="contact_show_list_nofinish"),  # 众筹精选(已完成)页面
    url(r'contact_book_show/(?P<book_id>.*)$', ContactBookShowView.as_view(), name="contact_book_show"),  # 已完成的众筹列表页面
    url(r'contact_book_show_id/(?P<book_show_code>.*)/$', ContactBookShowIdView.as_view(), name="contact_book_show_id"),# 已完成众筹详情页面

    url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),  # 配置上传文件的访问处理函数

    url(r'^ueditor/', include('DjangoUeditor.urls')),  # 富文本相关url
]
