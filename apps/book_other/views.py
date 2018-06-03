# # -*- coding: utf-8 -*-
# from django.shortcuts import render
# from django.views.generic.base import View#表示对类进行逻辑编写
#
# from .models import Comment
# from .forms import CommentForm
# from users.models import UserProfile
# from book_edit.models import EditAddDetails
# from utils.mixin_utils import LoginRequiredMixin
# # Create your views here.
#
#
# class ContactCommentView(View, LoginRequiredMixin):
#     """
#     用户评论
#     """
#     def post(self, request, comment_code):
#         comment = CommentForm(request.POST)
#         comment_code_id = EditAddDetails.objects.get(id=int(comment_code))
#
#         comment_all = comment_code_id.comment_set.all()
#         user_id = request.session.get('username_id')
#         user = UserProfile.objects.get(id=int(user_id))
#         if comment.is_valid():
#             content = request.POST.get("content", "")  # 获取用户评论的content
#             com_comment = Comment()
#             com_comment.com_content = content
#             com_comment.com_user = user
#             com_comment.con_edit = comment_code_id
#             com_comment.save()
#             return render(request, "contact_msg.html", {"msg": "发表成功", "comment_all": comment_all})
#
