# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-05 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0018_auto_20190505_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isshow',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a'),
        ),
        migrations.AlterField(
            model_name='article',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='\u6301\u7eed\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='article',
            name='introduction',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='\u6458\u8981'),
        ),
        migrations.AlterField(
            model_name='article',
            name='location',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='article',
            name='photoby',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='\u56fe\u7247\u6765\u6e90'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_person',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='\u53d1\u5e03\u8005'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='achievement',
            field=models.TextField(blank=True, null=True, verbose_name='\u6210\u5c31'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='course_teacher',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='\u6559\u6388\u8bfe\u7a0b'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='email',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='extratitle',
            field=models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='\u989d\u5916\u804c\u4f4d'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='hobby',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7231\u597d'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='introduction',
            field=models.TextField(verbose_name='\u7b80\u4ecb'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='moto',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4eba\u751f\u683c\u8a00'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='\u7535\u8bdd'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploadImages', verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='range_weight',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='\u663e\u793a\u6743\u91cd'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='school_name',
            field=models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='\u6bd5\u4e1a\u5b66\u6821'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='study_direction',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u7814\u7a76\u65b9\u5411'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='title',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='\u804c\u4f4d'),
        ),
    ]