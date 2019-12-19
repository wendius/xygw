"""dingli_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url( r'^static/(?P<path>.*)$', serve,{ 'document_root': settings.STATIC_URL }),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'', include('django_web.urls')),
]

handler404 = "app.views.views.page_not_found"
handler500 = "app.views.views.page_error"
