from django.contrib import admin

# Register your models here.
from blog.models import ArticleCategory, Article, ArticleTag, BigCategory, Banner, Keywords, FriendLink, Notice


class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'add_time')
    list_display_links = ['name']
    fields = ['name']


class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'add_time')
    list_display_links = ['name']
    fields = ['name']


class BigCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'add_time')
    list_display_links = ['name']
    fields = ['name', 'slug']


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'bigCategory', 'add_time')
    list_display_links = ['name']
    fields = ['bigCategory', 'name', 'slug']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'show_author', 'category', 'add_time', 'show_tag')
    list_display_links = ['id']
    list_editable = ('title',)
    search_fields = ['title','author__name']
    fields = ['category', 'tag', 'keywords', 'title', 'description', 'body', 'image']
    list_filter = ('add_time', 'category')
    list_per_page = 30
    date_hierarchy = 'add_time'

    def show_author(self, obj):
        return obj.author.name
    show_author.short_description = '作者'

    def show_tag(self, obj):
        return [ta.name for ta in obj.tag.all()]
    show_tag.short_description = '标签'

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    # def get_image_name(self, obj):
    #     image = datetime.now().strftime('%Y%m%d%H%M%S') + obj.image
    #     return image

    filter_horizontal = ('tag', 'keywords')


class BannerAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'content', 'image', 'url')


class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'link', 'is_active', 'is_show', 'add_date')


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'is_active', 'add_date')


admin.site.site_title = "管理系统"
admin.site.site_header = "Blog后台管理系统"


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
admin.site.register(BigCategory, BigCategoryAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Keywords, KeywordsAdmin)
admin.site.register(FriendLink, FriendLinkAdmin)
admin.site.register(Notice, NoticeAdmin)


