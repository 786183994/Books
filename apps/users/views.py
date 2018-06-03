# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render
from django.views.generic.base import View#表示对类进行逻辑编写
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .forms import LoginForm, RegisterForm
from utils.email_send import send_register_email
from .models import UserProfile, Banner,EmailVerifyRecord
from book_cover.models import Books, BookCollCard
from utils.mixin_utils import LoginRequiredMixin
from book_other.models import UserFavotion, UserClick, UserCooperation, UserFollow
from book_edit.models import EditAddDetails
from utils.random_number import book_certificates
from book_other.models import FixedFormat, SignInFollow


#邮箱也可以进行登录
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            #使用Q可以进行或逻辑的操作
            user = UserProfile.objects.get(Q(username = username)|Q(email=username))
            #验证密码
            if user.check_password(password):
                return user
        #不正确报异常
        except Exception as e:
            return None;


#邮箱激活
class ActiveUserView(View):
    #active_code表示默认给发送者发送的字符串，目的是为了安全性能的提高
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)

        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                #此方法最终要的就是设置该值为True
                user.is_active = True
                #再此生成作者的编号
                author_number = book_certificates()
                user.author_number = author_number
                #生成藏书证编号
                book_collection_card = book_certificates()

                book_coll_card = BookCollCard()
                book_coll_card.user = user
                book_coll_card.book_collection_card = book_collection_card

                book_coll_card.save()
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


#用户登录
class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        # 这里的else表示的是必要信息的填写
        if login_form.is_valid():
            # 获取登录时的username和password字段内容
            user_name = request.POST.get("username", "");
            pass_word = request.POST.get("password", "");
            # html中的csrf_token成功返回user对象,失败返回null
            user = authenticate(username=user_name, password=pass_word);
            if user is not None:
                #这里是对邮件是否被激活
                if user.is_active:
                    #进行登录验证
                    #login中还存在session的存储，就是给本次请求一个特定的id，存放在数据库表内。
                    login(request, user)
                    user_one = UserProfile.objects.get(username=user)
                    request.session['username_id'] = user_one.id
                    # 登陆成功跳转页面
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request,"login.html",{"msg":"用户未激活"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            # 否则跳转到本页面并返回错误信息
            return render(request, "login.html", {"login_form":login_form})


#用户注册
class RegisterView(View):
    #get请求数据时运行
    #get请求就是在进行页面的跳转工作
    def get(self, request):
        #添加验证码
        register_form = RegisterForm()
        return render(request, "register.html", {
            'register_form': register_form
        })

    #post请求数据时运行
    #post请求就是在进行数据的交互
    def post(self, request):
        register_form = RegisterForm(request.POST);#实例化form

        if register_form.is_valid():
            user_name = request.POST.get("email","")#获取页面登录时的username
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"msg": "该用户已经存在"})
            pass_word = request.POST.get("password","")#获取页面登录时的password
            user_profile = UserProfile();
            user_profile.username = user_name#设置页面信息中的username给数据库
            user_profile.email =user_name#设置页面信息中的email给数据库
            user_profile.is_active = False#设置为邮箱未激活状态
            user_profile.password = make_password(pass_word)#make_password表示将明文的密码改为不可阅读的密码
            # user_profile.save()#存进数据库
            #发送邮件
            css = send_register_email(user_name, "register")

            email_verify = EmailVerifyRecord()
            email_verify.email = user_name
            email_verify.code = css
            email_verify.send_type = "注册"
            email_verify.save()

            return render(request, "login.html")
        else:
            return render(request, "register.html",{
                "register_form": register_form,
            })


#用户登出
class LogoutView(View):
    """
    用户登出
    """
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


#用户登录首页
class IndexView(View):
    """
    项目的，首页
    """
    def get(self, request):
        #取出轮播图
        all_banners = Banner.objects.all().order_by('index')
        books = Books.objects.all()
        msg_code = 0
        has_fav_book = False#点赞
        has_click_book = False#收藏
        has_sign_in = True#签到

        if request.user.is_authenticated():
            for book in books:
                if UserFavotion.objects.filter(user=request.user, fav_id=book.id, fav_type=1):
                    has_fav_book = True

        if request.user.is_authenticated():
            for book in books:
                if UserFavotion.objects.filter(user=request.user, fav_id=book.id, fav_type=1):
                    has_click_book = True

        if request.user.is_authenticated():
            if SignInFollow.objects.filter(user=request.user, sign_in_end=1):
                has_sign_in = False

        # from book_other.models import RelationShip
        # user_id = request.session.get('username_id')
        # relationship = RelationShip.objects.filter(user_id=int(user_id))
        #
        # if relationship.is_payment == "paid":
        #     from Integral_block.models import Integral
        #     integral = Integral.objects.get(user_id=int(user_id))
        #     integral.integral_numbers = integral.integral_numbers + 2400
        #     integral.save()

        return render(request, "index.html", {
            "all_banners": all_banners,
            "has_fav_book": has_fav_book,
            "has_click_book": has_click_book,
            "msg_code": msg_code,
            "books": books,
            "has_sign_in": has_sign_in,
        })


#发送邮箱验证码
class SendEmailCodeView(LoginRequiredMixin, View):
    """
    发送邮箱验证码
    """
    def get(self,request):
        email = request.GET.get('email','')

        if UserProfile.objects.filter(email=email):
            return HttpResponse('{"email":"邮箱已存在"}', content_type='application/json')

        send_register_email(email,"update_email")
        return HttpResponse('{"status": "success"}', content_type='application/json')


#用户收藏
class AddFavView(View):
    """
    用户收藏，用户取消收藏
    """
    def post(self,request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type',0)

        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status": "fail", "msg":"用户未登录"}',  content_type='application/json');#{0}}.format(userask_form.errors),content_type='application/json'
        exist_records = UserFavotion.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            #如果已经存在，则表示用户取消收藏
            exist_records.delete()
            if int(fav_type) == 1:
                # books: 书籍；collection：收藏量
                books = Books.objects.get(id=int(fav_id))
                books.collection -= 1
                if books.collection < 0:
                    books.collection = 0
                books.collection_whether = "收藏"
                books.save()

            elif int(fav_type) == 2:
                #edit: 说说详情；collection：收藏量
                edit = EditAddDetails.objects.get(id=int(fav_id))
                edit.collection -= 1
                if edit.collection < 0:
                    edit.collection = 0
                edit.save()

            return HttpResponse('{"status": "success", "msg":"收藏"}',  content_type='application/json');#{0}}.format(userask_form.errors),content_type='application/json'

        else:
            user_fav = UserFavotion()
            if int(fav_id) >0 and int(fav_type)>0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()

                if int(fav_type) == 1:
                    books = Books.objects.get(id=int(fav_id))
                    books.collection += 1
                    books.collection_whether = "已收藏"
                    books.save()
                elif int(fav_type) == 2:
                    edit = EditAddDetails.objects.get(id=int(fav_id))
                    edit.collection += 1
                    edit.save()

                return HttpResponse('{"status": "success", "msg":"已收藏"}',content_type='application/json');  # {0}}.format(userask_form.errors),content_type='application/json'

            else:
                return HttpResponse('{"status": "fail", "msg":"收藏出错"}',content_type='application/json');  # {0}}.format(userask_form.errors),content_type='application/json'


#用户点赞
class ClickFavView(View):
    """
    用户点赞，用户取消点赞
    """
    def post(self,request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status": "fail", "msg":"用户未登录"}',  content_type='application/json');#{0}}.format(userask_form.errors),content_type='application/json'
        exist_records = UserClick.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            #如果已经存在，则表示用户取消点赞
            exist_records.delete()
            books = Books.objects.get(id=int(fav_id))
            edit = EditAddDetails.objects.get(id=int(fav_id))
            if int(fav_type) == 1:
                # books: 书籍；fav_point：点赞量
                books.fav_point -= 1
                if books.fav_point < 0:
                    books.fav_point = 0
                books.fav_whether = "点赞"
                books.save()

            elif int(fav_type) == 2:
                #edit: 说说详情；fav_point：点赞量

                edit.fav_point -= 1
                if edit.fav_point < 0:
                    edit.fav_point = 0
                edit.fav_whether = "点赞"
                edit.save()

            return HttpResponse('{"status": "success", "msg":"点赞"}',  content_type='application/json');#{0}}.format(userask_form.errors),content_type='application/json'

        else:
            user_fav = UserClick()
            if int(fav_id) >0 and int(fav_type)>0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()

                if int(fav_type) == 1:
                    #书籍
                    books = Books.objects.get(id=int(fav_id))
                    books.fav_point += 1
                    books.fav_whether = "已点赞"
                    books.save()

                elif int(fav_type) == 2:
                    #说说
                    edit = EditAddDetails.objects.get(id=int(fav_id))
                    edit.fav_point += 1
                    edit.fav_whether = "已点赞"
                    edit.save()

                return HttpResponse('{"status": "success", "msg":"已点赞"}',content_type='application/json');  # {0}}.format(userask_form.errors),content_type='application/json'

            else:
                return HttpResponse('{"status": "fail", "msg":"点赞出错"}',content_type='application/json');  # {0}}.format(userask_form.errors),content_type='application/json'


class FollowFavView(View):
    """
     用户关注，用户取消关注
     """

    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status": "fail", "msg":"用户未登录"}',
                                content_type='application/json');  # {0}}.format(userask_form.errors),content_type='application/json'
        exist_records = UserFollow.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 如果已经存在，则表示用户取消点赞
            exist_records.delete()
            books = Books.objects.get(id=int(fav_id))
            edit = EditAddDetails.objects.get(id=int(fav_id))
            if int(fav_type) == 1:
                # books: 书籍；fav_point：点赞量
                books.fav_point -= 1
                if books.fav_point < 0:
                    books.fav_point = 0
                books.fav_whether = "点赞"
                books.save()

            elif int(fav_type) == 2:
                # edit: 说说详情；fav_point：点赞量

                edit.fav_point -= 1
                if edit.fav_point < 0:
                    edit.fav_point = 0
                edit.follow_whether = "关注"
                edit.fav_whether = "点赞"
                edit.save()

            return HttpResponse('{"status": "success", "msg":"关注"}',
                                content_type='application/json');  # {0}}.format(userask_form.errors),content_type='application/json'

        else:
            user_fav = UserFollow()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()

                if int(fav_type) == 1:
                    # 书籍
                    books = Books.objects.get(id=int(fav_id))
                    books.fav_point += 1
                    books.fav_whether = "已点赞"
                    books.save()

                elif int(fav_type) == 2:
                    # 说说
                    edit = EditAddDetails.objects.get(id=int(fav_id))
                    edit.fav_point += 1
                    edit.follow_whether = "已关注"
                    edit.fav_whether = "已点赞"
                    edit.save()

                return HttpResponse('{"status": "success", "msg":"已关注"}',
                                    content_type='application/json');  # {0}}.format(userask_form.errors),content_type='application/json'

            else:
                return HttpResponse('{"status": "fail", "msg":"关注出错"}',
                                    content_type='application/json');  # {0}}.format(userask_form.errors),content_type='application/json'


#我的主页面
class UsersView(View):
    """
    个人中心主页面
    """
    def get(self, request):
        user_id = request.session.get('username_id')
        user = UserProfile.objects.get(id=int(user_id))

        return render(request, "users.html", {
            "user": user,
        })


class UserCangShuZhengView(View):
    """
        藏书证显示
    """
    def get(self, request):
        user_id = request.session.get('username_id')
        user = UserProfile.objects.get(id=int(user_id))
        book_cards = BookCollCard.objects.filter(user=request.user)

        books = Books.objects.all()
        explain = FixedFormat.objects.all()
        return render(request, "cangshuzheng.html", {
            "user": user,
            "books": books,
            "book_cards": book_cards,
            "explain": explain,
        })


class UserShouCangPinView(View):
    """
        收藏品
    """
    def get(self, request):
        books = Books.objects.all()

        return render(request, "shoucangpin.html", {"books": books})


class UserOnTheCollectionPinView(View):
    """
    关于收藏品
    """
    def get(self, request):
        explain = FixedFormat.objects.all()#藏书证说明
        books = Books.objects.all()#出版的书籍
        return render(request, "guanyushoucangpin.html", {
            "explain": explain,
            "books": books,
        })


class UserOnThegOurView(View):
    """
    关于我们
    """
    def get(self, request):
        company = FixedFormat.objects.all()
        cooperations = UserCooperation.objects.all()#合作商

        return render(request, "guanyuwomen.html", {
            "company": company,
            "cooperations": cooperations,
        })


class PictureUploadView(View):
    """
    图片上传
    """
    def get(self, request):
        pass
    def post(self, request):
        pass
