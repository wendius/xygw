# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import datetime
from ..models import Article,TeacherInfo,TeacherCategory
# Create your views here.
def index(request):
    context = {}
    # list = ["a", "b", "c", "d"]
    # for i in list:
    #     print i
    Article_list = Article.objects.all().order_by('-publish_date')[:3]
    Leader_list = TeacherCategory.objects.get(category='领导').teacher.all().order_by('-range_weight')[:4]

    for i in Leader_list:
        print i
    return render(request, 'index.html', {'list': Article_list,'Leader_list': Leader_list})

def test(request):
    return render_to_response('articlesnew.html')

def enroll(request):
    return render_to_response('enroll.html')