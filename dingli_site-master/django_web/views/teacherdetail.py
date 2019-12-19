# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from ..models import TeacherInfo
# Create your views here.
def index(request,id):
    teacher = TeacherInfo.objects.get(id=id)
    context = {'teacher': teacher}
    # teacher.id = teacher.id + 1
    # teacher.save()
    # print teacher.name
    return render(request, 'teacher_detail.html', context)
