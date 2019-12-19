# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from ..models import TeacherInfo,TeacherCategory
# Create your views here.
category_map = {
    "teacher":"老师",
    "leader":"领导",
    "instructor":"辅导员",
    "party":"党员",
    "administration":"行政团队",
    "export": "专家团队"
}

show_category_map = {
    "teacher":"专业老师",
    "leader":"领导",
    "instructor":"辅导员",
    "party":"党员",
    "administration":"行政团队",
    "export":"专家团队"
}

def index(request,category):
    # teacher = TeacherInfo.objects.get(id=0)
    # context = {'teacher': teacher}
    temp = category_map.get(category, None)
    show_categor = show_category_map.get(category, None)

    if temp == None:
        return render(request, '404.html')
    else:
        list = TeacherCategory.objects.get(category=category_map.get(category, None)).teacher.all()
        # for e in list:
        #     print (e.id)
        return render(request, 'teacher.html', {'results': list,'category': show_categor})
    # teacher.id = teacher.id + 1
    # teacher.save()



