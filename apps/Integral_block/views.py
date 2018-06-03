# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View#表示对类进行逻辑编写

from users.models import UserProfile
from book_other.models import FixedFormat, SignInFollow
# Create your views here.


class SignInView(View):
    """
        首页的签到
    """
    def get(self, request):
        from Integral_block.models import Integral, Grade
        import random
        #获取当前用户，通过session中的username_id
        user_id = request.session.get('username_id')
        user = UserProfile.objects.get(id=int(user_id))
        # 积分表，  为了加积分
        integral = Integral.objects.get(user_id=int(user_id))
        integral.integral_numbers = integral.integral_numbers + random.randint(2,5)
        integral.save()

        #等级表，  为了显示等级
        grade = Grade.objects.get(user_id=int(user_id))

        #获取有关我的权限的说明
        fixedformat = FixedFormat.objects.all()
        #积分须知
        increase_integral=""
        #权限说明
        jurisdiction_explain=""
        for fixed in fixedformat:
            increase_integral = fixed.increase_integral
            jurisdiction_explain= fixed.jurisdiction_explain

        #签到功能
        import time
        import datetime
        # 今天日期
        today = datetime.date.today()

        # 明天时间
        tomorrow = today + datetime.timedelta(days=1)

        # 昨天结束时间戳
        yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1

        # 今天开始时间戳
        today_start_time = yesterday_end_time + 1

        # 今天结束时间戳
        today_end_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1

        time = time.time()  # 浮点时间

        if time > today_start_time and time < today_end_time:
            sign_in = SignInFollow()
            if sign_in.sign_in_end == 0:
                sign_in.user = user
                sign_in.sign_in = 1
                sign_in.sign_in_end = 1
                sign_in.save()

        return render(request, "quanxian.html", {
            "integral": integral,
            "grade": grade,
            "increase_integral": increase_integral,
            "jurisdiction_explain": jurisdiction_explain,
        })


class JurisdictionView(View):
    """
        用户首页点击我的权限
    """
    def get(self, request):
        from Integral_block.models import Integral, Grade
        #获取当前用户，通过session中的username_id
        user_id = request.session.get('username_id')
        user = UserProfile.objects.get(id=int(user_id))
        # 积分表
        integral = Integral.objects.get(user_id=int(user_id))
        #等级表，  为了显示等级
        grade = Grade.objects.get(user_id=int(user_id))
        #获取有关我的权限的说明
        fixedformat = FixedFormat.objects.all()
        #积分须知
        increase_integral=""
        #权限说明
        jurisdiction_explain=""
        for fixed in fixedformat:
            increase_integral = fixed.increase_integral
            jurisdiction_explain= fixed.jurisdiction_explain

        return render(request, "quanxian.html", {
            "integral": integral,
            "grade": grade,
            "increase_integral": increase_integral,
            "jurisdiction_explain": jurisdiction_explain,
        })