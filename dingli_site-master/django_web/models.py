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
        ('export', '专家团队'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(u'姓名',max_length=16)
    title = models.CharField(u'职位',max_length=16, null=True, blank=True)
    extratitle = models.CharField(u'额外职位',max_length=16,default="", null=True, blank=True) #用于detail页面展示
    grade = models.CharField(u'学历',max_length=16,default="")
    school_name = models.CharField(u'毕业学校',max_length=16,default="", null=True, blank=True)
    phone = models.CharField(u'电话',max_length=16, null=True, blank=True)
    email = models.CharField(u'邮箱',max_length=32, null=True, blank=True)
    moto = models.CharField(u'人生格言',max_length=32, null=True, blank=True)
    work_experice = models.CharField(u'工作经历',max_length=32)
    hobby = models.CharField(u'爱好',max_length=32, null=True, blank=True)
    course_teacher = models.CharField(u'教授课程', max_length=64,default="", null=True, blank=True)
    study_direction = models.CharField(u'研究方向',max_length=64, null=True, blank=True)
    introduction = models.TextField(u'简介')
    achievement = models.TextField(u'成就', null=True, blank=True)
    range_weight = models.IntegerField(u'显示权重', default=0, null=True, blank=True) #显示顺序
    photo = models.ImageField(u'图片', upload_to='uploadImages',default="", null=True, blank=True)
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
    teacher = models.ManyToManyField(TeacherInfo, blank=True, verbose_name="老师姓名")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = u'老师分类'
        verbose_name_plural = u'老师分类'

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
    publish_date = models.DateTimeField(u'发布日期',blank=True, auto_now_add = False, )#default=datetime.now(),
    publish_person = models.CharField(u'发布者',max_length=64,default="", null=True, blank=True)
    introduction = models.CharField(u'摘要',max_length=128, default="", null=True, blank=True)
    photoby = models.CharField(u'图片来源',max_length=64,default="", null=True, blank=True)
    location = models.CharField(u'地址',max_length=64,default="", null=True, blank=True)
    duration = models.CharField(u'持续时间',max_length=64, default="", null=True, blank=True) #持续时间
    isshow = models.BooleanField(u'是否显示', default=True)
    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = u'新闻'

class ArticleCategory(models.Model):
    category = models.CharField('新闻分类', max_length=10)
    article = models.ManyToManyField(Article, blank=True, verbose_name="新闻")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = u'新闻分类'
        verbose_name_plural = u'新闻分类'

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    fieldsets = (
        (None, {'fields': ('category', 'article')}),
    )
    filter_horizontal = ('article',)
