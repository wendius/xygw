# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from ..models import Article
# Create your views here.
def index(request,id):
    article = Article.objects.get(id=id)
    context = {'article': article}
    # article.id = article.id + 1
    # article.save()
    # print article.id
    return render(request, 'article.html',context)
