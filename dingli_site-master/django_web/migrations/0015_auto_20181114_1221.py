# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-14 12:21
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0014_article_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u6b63\u6587'),
        ),
    ]