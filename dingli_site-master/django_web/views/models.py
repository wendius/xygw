# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models
from datetime import datetime
import sys;

reload(sys);
sys.setdefaultencoding("utf8")
# Create your models here.
class TeacherInfo(models.Model):
    Category_CHOICES = (
        ('leader', '领导'),
        ('teacher', '老师'),
        ('instructor', '辅导员'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(u'姓名',max_length=16)
    title = models.CharField(u'职位',max_length=16)
    extratitle = models.CharField(u'职位',max_length=16,default="") #用于detail页面展示
    grade = models.CharField(u'学历',max_length=16,default="")
    school_name = models.CharField(u'毕业学校',max_length=16,default="")
    phone = models.CharField(u'电话',max_length=16)
    email = models.CharField(u'邮箱',max_length=32)
    moto = models.CharField(u'人生格言',max_length=32)
    work_experice = models.CharField(u'工作经历',max_length=32)
    hobby = models.CharField(u'爱好',max_length=32)
    course_teacher = models.CharField(u'教授课程', max_length=64,default="")
    study_direction = models.CharField(u'研究方向',max_length=64)
    introduction = models.TextField()
    achievement = models.TextField()
    range_weight = models.IntegerField(default=0) #显示顺序
    photo = models.ImageField(u'图片', upload_to='uploadImages',default="")
    # labels = models.ArrayField(
    #     models.CharField(max_length=32, blank=True, choices=Category_CHOICES),
    #     default=list,
    #     blank=True,
    # )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'老师信息'
        verbose_name_plural = u'老师信息'
        db_table = 'django_web_teacherinfo'

class TeacherCategory(models.Model):
    category = models.CharField('老师分类', max_length=10)
    teacher = models.ManyToManyField(TeacherInfo, blank=True)

class TeacherCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    fieldsets = (
        (None, {'fields': ('category', 'teacher')}),
    )
    filter_horizontal = ('teacher',)


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    content = RichTextUploadingField('正文')
    title = models.CharField(u'标题',max_length=64,default="")
    title_pic = models.ImageField(u'头部图片', upload_to='uploadImages',default="")
    publish_date = models.DateTimeField(blank=True, auto_now_add = True, )#default=datetime.now(),
    publish_person = models.CharField(max_length=64,default="")
    introduction = models.CharField(max_length=128, default="")
    photoby = models.CharField(max_length=64,default="")
    location = models.CharField(max_length=64,default="")
    duration = models.CharField(max_length=64, default="") #持续时间
    def __str__(self):
        return self.title

class ArticleCategory(models.Model):
    category = models.CharField('新闻分类', max_length=10)
    article = models.ManyToManyField(Article, blank=True)

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    fieldsets = (
        (None, {'fields': ('category', 'article')}),
    )
    filter_horizontal = ('article',)