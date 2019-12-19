# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from ..models import TeacherInfo,TeacherCategory,ArticleCategory,Article
# Create your views here.
category_map = {
    "hot":"热点新闻",
    "all": "新闻中心",
    "party":"党团工作",
    "international": "国际化教育",
    "job": "就业工作",
    "student": "学生成长",
    "work": "招生工作",
    "industry": "行业新闻",
    "notice": "通知公告",
    "team": "产学合作", 
    "star": "实习明星"
}

show_category_map = {
    "hot":"热点新闻",
    "all": "新闻中心",
    "party": "党团工作",
    "international": "国际化教育",
    "job": "就业工作",
    "student": "学生成长",
    "work": "招生工作",
    "industry": "行业新闻",
    "notice": "通知公告",
    "team": "产学合作",
    "star": "实习明星"


}

def index(request,category):
    # teacher = TeacherInfo.objects.get(id=0)
    # context = {'teacher': teacher}
    temp = category_map.get(category, None)
    show_categor = show_category_map.get(category, None)

    if temp == None:
        return render(request, '404.html')
    else:
        if category_map.get(category) == '党团工作' \
                or category_map.get(category) == '就业工作' or category_map.get(category) == '学生成长' \
                or category_map.get(category) == '招生工作' or category_map.get(category) == '国际化教育' \
                or category_map.get(category) == '热点新闻' or category_map.get(category) == '行业新闻' or category_map.get(category) == '通知公告' or category_map.get(category) == '产学合作' or category_map.get(category) == '实习明星':
            # Article_list = Article.objects.all()
            Article_list = ArticleCategory.objects.get(category=category_map.get(category, None)).article.filter(isshow=1).order_by("-publish_date")
            paginator = Paginator(Article_list, 20)  # Show 25 contacts per page

            page = request.GET.get('page',1)
            try:
                Articles = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Articles = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Articles = paginator.page(paginator.num_pages)

            return render(request, 'articlesnew.html', {'Articles': Articles, 'category': show_categor})
        else:
            Article_list = Article.objects.filter(isshow=1).order_by('-publish_date')
            paginator = Paginator(Article_list, 20)  # Show 25 contacts per page

            page = request.GET.get('page',1)
            try:
                Articles = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Articles = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Articles = paginator.page(paginator.num_pages)
            # for e in Article_list:
            #     print (e.id)
            return render(request, 'articlesnew.html', {'Articles': Articles,'category': show_categor})
    # teacher.id = teacher.id + 1
    # teacher.save()



