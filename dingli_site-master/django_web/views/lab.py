from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.


def index(request,special):
    context = {}
    url_map = {
        "1": 'lab/1.html',
        "2": 'lab/2.html',
        "3": 'lab/3.html',
        "4": 'lab/4.html',
        "5": 'lab/5.html',
        "6": 'lab/6.html',
        "7": 'lab/7.html',
        "8": 'lab/8.html',
        "9": 'lab/9.html',
	"10": 'lab/10.html',
	"11": 'lab/11.html',
	"12": 'lab/12.html',
	"13": 'lab/13.html',
	"14": 'lab/14.html'

    }
    return render(request, url_map.get(special, "404.html"), context)
