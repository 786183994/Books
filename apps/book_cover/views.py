# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View#表示对类进行逻辑编写

from .models import PublicTable, Books
from book_other.models import UserFavotion, RelationShip
from book_edit.models import BookDetails
from users.models import Banner
from users.models import UserProfile
from book_cover.models import BookCollCard
# Create your views here.


class ContactShowView(View):
    """
    众筹详情
    """
    def get(self, request, show_code):
        public = PublicTable.objects.get(id=int(show_code))
        bookdetails = BookDetails.objects.filter(book_id__in=show_code)
        user_id = request.session.get('username_id')
        bookcollcard = BookCollCard.objects.get(user_id=int(user_id))
        author_num = bookcollcard.book_collection_card

        relation = RelationShip.objects.get(user_id=int(user_id), book_id=int(show_code))
        return render(request, "contact_show.html", {
            "bookdetails": bookdetails,
            "public": public,
            "author_num": author_num,
            "relation": relation,
        })


class ContactBookShowView(View):
    """
    已完成的众筹列表页面
    """
    def get(self, request, book_id):

        bookdetails = BookDetails.objects.filter(book_id__in=book_id)
        return render(request, "contact_book_content.html", {
            "bookdetails": bookdetails,
        })


class ContactBookShowIdView(View):
    """
    已完成的众筹详情页面
    """
    def get(self, request, book_show_code):
        bookdetails = BookDetails.objects.get(id=int(book_show_code))
        book_id = bookdetails.book_id
        return render(request, "contact_book_msg.html", {
            "bookdetails": bookdetails,
            "show_code": book_id,
        })


class ContactShowListView(View):
    """
    众筹精选页面（即众筹完成书籍页面）
    """
    def get(self, request, msg_code):
        books = Books.objects.all()
        all_banners = Banner.objects.all().order_by('index')

        has_fav_book = False
        has_click_book = False
        if request.user.is_authenticated():
            for book in books:
                if UserFavotion.objects.filter(user=request.user, fav_id=book.id, fav_type=1):
                    has_fav_book = True

        if request.user.is_authenticated():
            for book in books:
                if UserFavotion.objects.filter(user=request.user, fav_id=book.id, fav_type=1):
                    has_click_book = True

        return render(request, "index.html", {
            "all_banners": all_banners,
            "books": books,
            "msg_code": msg_code,
            "has_fav_book": has_fav_book,
            "has_click_book": has_click_book,
        })


class ContactShowListUnfinishedView(View):
    """
    众筹未完成页面
    """
    def get(self, request, msg_code):
        books = Books.objects.all()
        all_banners = Banner.objects.all().order_by('index')

        has_fav_book = False
        has_click_book = False
        if request.user.is_authenticated():
            for book in books:
                if UserFavotion.objects.filter(user=request.user, fav_id=book.id, fav_type=1):
                    has_fav_book = True

        if request.user.is_authenticated():
            for book in books:
                if UserFavotion.objects.filter(user=request.user, fav_id=book.id, fav_type=1):
                    has_click_book = True

        return render(request, "index.html", {
            "all_banners": all_banners,
            "books": books,
            "msg_code": msg_code,
            "has_fav_book": has_fav_book,
            "has_click_book": has_click_book,
        })