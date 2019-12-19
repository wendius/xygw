# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from ..models import Article,TeacherInfo,TeacherCategory
# Create your views here.


def index(request,category):
    context = {}
    Leader_list = TeacherCategory.objects.get(category='领导').teacher.all().order_by('-range_weight')[:4]
    url_map = {
        "1": 'introduction1.html',
        "2": 'introduction2.html',
        "3": 'introduction3.html',
        "4": 'introduction4.html',
        "5": 'introduction5.html'
    }
    return render(request, url_map.get(category,"404.html"), {'Leader_list': Leader_list})
    # return render(request, 'index.html', context)
