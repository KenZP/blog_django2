"""newblog URL Configuration

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
#from django.conf.urls import url, include
from django.urls import path, re_path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView
from django.views.static import serve

from blog.sitemaps import ArticleSitemap, TagSitemap, CategorySitemap
from newblog.settings import MEDIA_ROOT#, STATIC_ROOT

# 网站地图
sitemaps = {
    'articles': ArticleSitemap,
    'tags': TagSitemap,
    'categories': CategorySitemap
}

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include("blog.urls", namespace="blog")),
    re_path(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    #url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    re_path(r'^captcha/', include('captcha.urls')),
    # 富文本相关url
    re_path(r'^ueditor/', include('DjangoUeditor.urls')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  # 网站地图
    # favicon.cio
    re_path(r'^favicon\.ico$',RedirectView.as_view(url=r'static/images/blog.ico')),
]

# 全局404页面配置
#handler404 = 'blog.views.page_not_found'
# handler500 = 'blog.views.page_error'
