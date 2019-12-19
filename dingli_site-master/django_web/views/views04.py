from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.


def index(request, category):
    context = {}
    url_map = {
        "1": 'menu4_1.html',
        "2": 'menu4_2.html',
        "3": 'menu4_3.html',
        "4": 'menu4_4.html'
    }
    return render(request, url_map.get(category, "404.html"), context)

def lab(request):
    return render(request, "lab.html")
