from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.


def index(request,special):
    context = {}
    url_map = {
        "1": 'special/1.html',
        "2": 'special/2.html',
        "3": 'special/3.html',
        "4": 'special/4.html',
        "5": 'special/5.html',
        "6": 'special/6.html'
    }
    return render(request, url_map.get(special,"404.html"), context)