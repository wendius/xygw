# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def class1(request):
    return render(request, 'testclass/class1.html')

def class2(request):
    return render(request, 'testclass/class2.html')