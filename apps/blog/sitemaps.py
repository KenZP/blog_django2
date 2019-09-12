# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from .models import Article, ArticleCategory, ArticleTag # BigCategory
# from django.db.models.aggregates import Count


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0
    protocol = None

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        if obj.update_date:
            return obj.update_date
        return obj.add_time


# class BigCategorySitemap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.8
#
#     def items(self):
#         return BigCategory.objects.all()
#         # return ArticleCategory.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)
#
#     def lastmod(self, obj):
#         return obj.add_time
#         # return obj.article_set.first().add_time


class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = None

    def items(self):
        return ArticleCategory.objects.all()
        # return ArticleCategory.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)

    def lastmod(self, obj):
        return obj.add_time
        # return obj.article_set.first().add_time


class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = None

    def items(self):
        return ArticleTag.objects.all()
        # return ArticleTag.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)


    def lastmod(self, obj):
        return obj.add_time
        # return obj.article_set.first().add_time
