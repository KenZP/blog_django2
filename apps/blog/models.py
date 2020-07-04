import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

from newblog import settings
from users.models import UserPro

from DjangoUeditor.models import UEditorField

# Create your models here.


# 文章关键词
class Keywords(models.Model):
    name = models.CharField(max_length=30, default="", verbose_name='文章关键词')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '关键词'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    name = models.CharField(max_length=20, default="", verbose_name="文章标签")
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def get_article_list(self):
        """返回当前标签下所有发表的文章列表"""
        return Article.objects.filter(tag=self)

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'tag_name': self.name})

    def __str__(self):
        return self.name


class BigCategory(models.Model):
    name = models.CharField(max_length=10, default="", verbose_name="大分类")
    slug = models.SlugField(unique=True, default="",verbose_name="大分类唯一标识")
    is_active = models.BooleanField(default=True, blank=True, verbose_name='是否在菜单栏显示')
    description = models.TextField(max_length=240, default=settings.SITE_DESCRIPTION, verbose_name='大分类描述',
                                   help_text='用来作为SEO中description,长度参考SEO标准')
    keywords = models.TextField(verbose_name='关键字', max_length=240, default=settings.SITE_KEYWORDS,
                                help_text='用来作为SEO中keywords,长度参考SEO标准')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "大分类"
        verbose_name_plural = verbose_name

    def get_article_category(self):
        return self.articlecategory_set.all()

    def get_big_category_article(self):
        categories = self.articlecategory_set.all()
        all_articles = Article.objects.none()
        for category in categories:
            articles = category.article_set.all()
            all_articles = all_articles | articles
        return all_articles

    def get_absolute_url(self):
        return reverse('blog:big_category', kwargs={'big_slug': self.slug})

    def __str__(self):
        return self.name


class ArticleCategory(models.Model):
    bigCategory = models.ForeignKey(BigCategory, default="", verbose_name="大分类", on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=10, default="", verbose_name="文章分类")
    description = models.TextField(verbose_name='描述', max_length=240, default=settings.SITE_DESCRIPTION,
                                   help_text='用来作为SEO中description,长度参考SEO标准')
    slug = models.SlugField(unique=True, default="", verbose_name="分类唯一标识")
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name

    def get_category_article(self):
        return self.article_set.all()

    def get_absolute_url(self):
        return reverse('blog:article_category', kwargs={'big_slug': self.bigCategory.slug, 'category_slug': self.slug})

    def __str__(self):
        return self.name


class Article(models.Model):
    # big_category = models.ForeignKey(BigCategory, default="", verbose_name="文章大分类")
    category = models.ForeignKey(ArticleCategory, default="",verbose_name="文章分类", on_delete=models.SET_DEFAULT)
    # slug = models.SlugField(unique=True, default="", verbose_name="文章唯一标识")
    tag = models.ManyToManyField(ArticleTag, default="",verbose_name="标签")
    keywords = models.ManyToManyField(Keywords, default="", blank=True, verbose_name="关键字")
    author = models.ForeignKey(UserPro, default="", verbose_name="作者", on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=30, default="", verbose_name="文章标题")
    description = models.TextField(default="", blank=True, verbose_name="文章简介")
    body = models.TextField(default="", verbose_name="文章内容")
    # body = UEditorField(width=900, height=600, toolbars="full", default="", imagePath="images/%(basename)s_%(datetime)s.%(extname)s",
    #                     filePath="files/",verbose_name="文章内容")
    # body = RichTextUploadingField(default='', verbose_name="文章内容")
    image = models.ImageField(upload_to="article/%Y/%m", default="", verbose_name="文章封面", max_length=100)
    read_nums = models.IntegerField(default=0, verbose_name="浏览人数")
    content_nums = models.IntegerField(default=0, verbose_name="评论数")
    like_nums = models.IntegerField(default=0, verbose_name="喜欢数")
    # is_hot = models.BooleanField(default=False, verbose_name="是否热门专题")
    # is_banner = models.BooleanField(default=False, verbose_name="是否轮播")
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
    update_date = models.DateTimeField(verbose_name='修改时间', default=datetime.datetime.now)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

    def save(self, *args, **kwargs):
        self.update_date = datetime.datetime.now()
        super().save(*args, **kwargs)

    def get_week_time(self):
        return (datetime.datetime.now() - self.add_time).days // 7

    def get_tag_article(self):
        all_article = Article.objects.none()
        for tag in self.tag.all():
            articles = Article.objects.filter(tag=tag)
            all_article = all_article | articles
        # all_articles = all_articles.order_by('-add_time')[:4]
        return all_article

    def get_article_tag(self):
        return self.tag.all()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


# 轮播图
class Banner(models.Model):
    number = models.IntegerField(verbose_name='编号', help_text='编号决定图片播放的顺序，图片不要多于5张')
    title = models.CharField(verbose_name='标题', max_length=20, blank=True, null=True, help_text='标题可以为空')
    content = models.CharField(verbose_name='描述', max_length=80)
    image = models.ImageField(upload_to="banner/%Y/%m", default="", max_length=300, verbose_name="图片")
    img_url = models.CharField(verbose_name='图片地址', default="#", max_length=200, help_text="如果把资源放在第三方储存里，这里写图片地址")
    url = models.CharField(verbose_name='跳转链接', max_length=200, default='#', help_text='图片跳转的超链接，默认#表示不跳转')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
        # 编号越小越靠前，添加的时间约晚约靠前
        ordering = ['number', '-id']

    def __str__(self):
        return self.content[:25]


class FriendLink(models.Model):
    name = models.CharField(verbose_name='网站名称', max_length=50)
    description = models.CharField(verbose_name='网站描述', max_length=100, blank=True)
    link = models.URLField(verbose_name='友链地址', help_text='请填写http或https开头的完整形式地址')
    logo = models.URLField(verbose_name='网站LOGO', help_text='请填写http或https开头的完整形式地址', blank=True)
    add_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='是否有效', default=True)
    is_show = models.BooleanField(verbose_name='是否首页展示', default=False)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['add_date']

    def __str__(self):
        return self.name


# 公告
class Notice(models.Model):
    text = models.TextField(verbose_name='公告', default=settings.NOTICE, null=True)
    is_active = models.BooleanField(verbose_name='是否开启', default=False)
    add_date = models.DateTimeField(verbose_name='提交日期', auto_now_add=True)

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = verbose_name
        ordering = ['add_date']

    def __str__(self):
        return self.text