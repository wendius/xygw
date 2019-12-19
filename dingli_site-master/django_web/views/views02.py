from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.


def index(request,category):
    context = {}
    url_map = {
        "1": 'introduction1.html',
        "2": 'introduction2.html'
    }
    return render(request, url_map.get(category,"404.html"), context)
    # return render(request, 'index.html', context)
