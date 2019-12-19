# coding=utf-8
import xadmin
from .models import TeacherInfo,TeacherCategory,Article,ArticleCategory

class TeacherAdmin(object):
    list_display = ['id', 'name', 'title', 'extratitle', 'grade',
                    'school_name']
    search_fields = ['name', ]
    list_editable = ['id', 'name', 'title', 'extratitle', 'grade',
                     'school_name']
    list_filter = ['id', 'name', 'title', 'extratitle']

class AriticleAdmin(object):
    list_display = ['id', 'title', 'publish_date',
                    'publish_person', 'introduction', 'location', 'duration', 'isshow']
    search_fields = ['title', 'content']
    list_editable = [ 'title', 'publish_date',
                    'publish_person', 'introduction', 'location', 'duration', 'isshow']
    list_filter = ['id', 'title', 'content']


class TeacherCategoryAdmin(object):
    filter_horizontal = ('TeacherInfo',) #关联表
    style_fields = {'teacher': 'm2m_transfer'}

class ArticleCategoryAdmin(object):
    filter_horizontal = ('Article',) #关联表
    style_fields = {'article': 'm2m_transfer'}



from xadmin import views


class GlobalSetting(object):
    site_title = "鼎利学院后台管理系统"
    site_footer = "鼎利学院后台"


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(TeacherInfo, TeacherAdmin)
xadmin.site.register(TeacherCategory, TeacherCategoryAdmin)
xadmin.site.register(Article, AriticleAdmin)
xadmin.site.register(ArticleCategory, ArticleCategoryAdmin)
