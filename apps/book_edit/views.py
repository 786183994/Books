# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View#表示对类进行逻辑编写
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.defaultfilters import stringfilter

from users.models import Banner
from book_other.models import Comment
from book_other.forms import CommentForm
from users.models import UserProfile
from book_edit.models import EditAddDetails
from utils.mixin_utils import LoginRequiredMixin
from book_other.models import UserFavotion, UserClick
from .forms import EditForm
# Create your views here.


class ContactListView(View, LoginRequiredMixin):
    """
    话题列表页面
    """
    def get(self, request):
        all_banners = Banner.objects.all().order_by('index')#banner图
        user_id = request.session.get('username_id')
        user = UserProfile.objects.get(id=int(user_id))
        author_num = user.author_number
        edits = EditAddDetails.objects.filter(user=request.user).order_by("-add_time")#所有自己编写的说说

        #遍历当前登陆者的每条说说
        for edit in edits:
            #判断每条说说的点赞量是否大于88
            #如果大于，就给该用户积分+10
            #只要有一条大于就+10，两条+20，......
            if edit.fav_point >= 88:
                from Integral_block.models import Integral
                integral = Integral.objects.get(user_id=int(user_id))
                integral.integral_numbers = 10
                integral.save()

        return render(request, "contact_list.html",{
            "all_banners": all_banners,
            "edits": edits,
            "author_num": author_num,
        })


class ContactMsgView(View):
    """
    说说详情
    """
    def get(self, request, msg_code):
        edits = EditAddDetails.objects.get(id=int(msg_code))
        edit_up_id = edits.id - 1#上一页
        edit_down_id = edits.id + 1#下一页

        edits = EditAddDetails.objects.get(id=int(msg_code))
        comment_code_id = EditAddDetails.objects.get(id=int(msg_code))
        comment_all = comment_code_id.comment_set.all().order_by("-add_time")

        edit_all = EditAddDetails.objects.all()
        max_id = 0
        for edit in edit_all:
            if edit.id > max_id:
                max_id = edit.id
        print(max_id)
        if edit_up_id == 0:
            edit_up_id = None
        if edit_down_id > max_id:
            edit_down_id = None

        return render(request, "contact_msg.html", {
            "edits": edits,
            "comment_all": comment_all,
            "edit_up_id": edit_up_id,
            "edit_down_id": edit_down_id,
        })

    def post(self, request, msg_code):
        comment = CommentForm(request.POST)
        edits = EditAddDetails.objects.get(id=int(msg_code))
        comment_code_id = EditAddDetails.objects.get(id=int(msg_code))

        comment_all = comment_code_id.comment_set.all().order_by("-add_time")
        user_id = request.session.get('username_id')
        user = UserProfile.objects.get(id=int(user_id))
        if comment.is_valid():
            content = request.POST.get("content", "")  # 获取用户评论的content
            com_comment = Comment()
            com_comment.com_content = content
            com_comment.com_user = user
            com_comment.con_edit = comment_code_id
            com_comment.save()
            return render(request, "contact_msg.html", {
                "msg": "发表成功",
                "comment_all": comment_all,
                "edits": edits,
            })


class ContactNewestView(View):
    """
    最新的说说
    """
    def get(self, request):
        all_banners = Banner.objects.all().order_by('index')#banner图
        edits = EditAddDetails.objects.all().order_by("-add_time")#所有自己编写的说说

        return render(request, "contact_list.html",{
            "all_banners": all_banners,
            "edits": edits,
        })


class ContactSelectedView(View):
    """
    精选的说说
    """
    def get(self, request):
        all_banners = Banner.objects.all().order_by('index')#banner图
        edits = EditAddDetails.objects.all().order_by("-fav_point")#所有自己编写的说说

        return render(request, "contact_list.html",{
            "all_banners": all_banners,
            "edits": edits,
        })


class ContactFollowView(View):
    """
    关注的说说
    """
    def get(self, request, follow_code):
        all_banners = Banner.objects.all().order_by('index')#banner图
        edits = EditAddDetails.objects.all().order_by("-add_time")#所有自己编写的说说
        # user_id = request.session.get('username_id')
        # user = UserProfile.objects.get(id=int(user_id))
        # author_num = user.author_number#获取到作者编号

        return render(request, "contact_list.html",{
            "all_banners": all_banners,
            "edits": edits,
            "follow_code": follow_code,
        })


class ContactWriteView(View):
    """
        说说编辑
    """
    def get(self, request):
        return render(request, "contact_write.html", {})


class EditSayView(View):
    """
    编辑说说
    """
    def post(self, request):
        edit_form = EditForm(request.POST)
        user_id = request.session.get('username_id')
        user = UserProfile.objects.get(id=int(user_id))
        if edit_form.is_valid():
            # 获取登录时的username和password字段内容
            title = request.POST.get('title', 0)
            text = request.POST.get('text', 0)
            text = text[3:]
            text = text[:-4]

            edit_add = EditAddDetails()#说说详情页面
            edit_add.title = title#设置页面信息中的username给数据库
            edit_add.content =text#设置页面信息中的email给数据库
            edit_add.user = user#设置当前登陆者信息进入编辑页面
            edit_add.save()#存进数据库

            from Integral_block.models import Integral
            import random
            import time

            now_time = int(time.time())
            day_time = now_time - now_time % 86400 + time.timezone
            day_time_str = time.asctime(time.localtime(day_time))

            #获取当前登陆用户
            user_id = request.session.get('username_id')
            integral = Integral.objects.get(user_id=int(user_id))
            #这里增加的是普通说说的积分
            #普通说说一天内就可以增加四次
            #no play
            integral.integral_numbers = integral.integral_numbers + random.randint(0,6)
            integral.save()#加积分

            return HttpResponseRedirect(reverse("contact_list"))
        else:
            # 否则跳转到本页面并返回错误信息
            return render(request, "contact_write.html", {"edit_form": edit_form})


class ContactWriteHardcoverView(View):
    """
        众筹说说编辑
    """
    def get(self, request):
        return render(request, "contact_write_hardcover.html", {})


class EditSayHardcoverView(View):
    """
    编辑众筹说说
    """
    def post(self, request):
        edit_form = EditForm(request.POST)
        user_id = request.session.get('username_id')
        user = UserProfile.objects.get(id=int(user_id))
        if edit_form.is_valid():
            # 获取登录时的username和password字段内容
            title = request.POST.get('title', 0)
            text = request.POST.get('text', 0)
            text = text[3:]
            text = text[:-4]

            edit_add = EditAddDetails()#说说详情页面
            edit_add.title = title#设置页面信息中的username给数据库
            edit_add.content =text#设置页面信息中的email给数据库
            edit_add.user = user#设置当前登陆者信息进入编辑页面
            edit_add.save()#存进数据库

            from Integral_block.models import Integral
            import random
            import time

            # now_time = int(time.time())
            # day_time = now_time - now_time % 86400 + time.timezone
            # day_time_str = time.asctime(time.localtime(day_time))

            #获取当前登陆用户
            user_id = request.session.get('username_id')
            integral = Integral.objects.get(user_id=int(user_id))
            #这里增加的是众筹说说的积分
            integral.integral_numbers = integral.integral_numbers + 60
            integral.save()#加积分

            return HttpResponseRedirect(reverse("index"))
        else:
            # 否则跳转到本页面并返回错误信息
            return render(request, "contact_write_hardcover.html", {"edit_form": edit_form})