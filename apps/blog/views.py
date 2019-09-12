from django.core.paginator import Paginator, PageNotAnInteger
# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from .models import Article, BigCategory, ArticleCategory, Banner, ArticleTag


class IndexView(View):
    def get(self, request):
        articles = Article.objects.all()
        hot_articles = articles.order_by("-like_nums")[:5]
        left_big_banners = Banner.objects.filter(number__lte=5)
        # like_articles = articles.order_by("-read_nums")[:10]

        # big_categories = BigCategory.objects.all().order_by('add_time')
        # article_categories = ArticleCategory.objects.all()

        # 分页机制 Django1.11 官方文档
        # paginator = Paginator(contact_list, 25)  # Show 25 contacts per page
        #
        # page = request.GET.get('page')
        # try:
        #     contacts = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     contacts = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     contacts = paginator.page(paginator.num_pages)

        # 对文章进行分页
        try:
            page = request.GET.get('page', 1)  # 因为用get方法，如果get到的是空，就把1返回，所以下面的异常处理不需要考虑EmptyPage，只需处理PageNotAnInteger一场
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 10)  # Show 10 contacts per page

        all_articles = p.page(page)

        return render(request, "index.html", {
            'articles': all_articles,
            'hot_articles': hot_articles,
            'banner_articles': left_big_banners,
            # 'like_articles': like_articles
            # 'big_categorys': big_categories,
            # 'article_categorys': article_categories
        })


class IndexListView(ListView):
    template_name = 'index.html'
    context_object_name = 'articles'
    queryset = Article.objects.all()
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hot_articles'] = Article.objects.order_by("-like_nums")[:5]
        context['banner_articles'] = Banner.objects.filter(number__lte=5)
        return context


class BigCategoryView(View):
    def get(self, request, big_slug):
        big_category = BigCategory.objects.get(slug=big_slug)
        if big_slug == "resources":
            return render(request, 'resources.html', {
                "big_category": big_category
            })
        if big_slug == "about":
            return render(request, 'about.html', {
                "big_category": big_category
            })
        if big_slug == "message":
            return render(request, 'message.html', {
                "big_category": big_category
            })
        if big_slug == "reward":
            return render(request, 'reward.html', {
                "big_category": big_category
            })
        if big_slug == "exchange":
            return render(request, 'exchange.html', {
                "big_category": big_category
            })
        if big_slug == "question":
            return render(request, 'question.html', {
                "big_category": big_category
            })
        if big_slug == "cooperation":
            return render(request, 'cooperation.html', {
                "big_category": big_category
            })
        big_category = BigCategory.objects.get(slug=big_slug)
        all_articles = big_category.get_big_category_article()
        # all_articles = Article.objects.get(big_category=big_category)

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)  # 因为用get方法，如果get到的是空，就把1返回，所以下面的异常处理不需要考虑EmptyPage，只需处理PageNotAnInteger一场
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 10)  # Show 10 contacts per page

        all_articles = p.page(page)

        return render(request, 'categorypage.html', {
            "all_articles": all_articles,
            "big_category": big_category
        })


class BigCategoryListView(ListView):
    template_name = 'categorypage.html'
    context_object_name = 'all_articles'
    paginate_by = 2

    def get_queryset(self):
        big_category = BigCategory.objects.get(slug=self.kwargs.get('big_slug'))
        return big_category.get_big_category_article()

    def get_context_data(self, **kwargs):
        context = super(BigCategoryListView, self).get_context_data(**kwargs)
        context['big_category'] = BigCategory.objects.get(slug=self.kwargs.get('big_slug'))
        return context


class ResourcesView(View):
    def get(self, request):
        return render(request, 'resources.html', {
            'big_category':'resources'
        })


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {
            "big_category": 'about'
        })


class MessageView(View):
    def get(self, request):
        return render(request, 'message.html', {
            "big_category": 'message'
        })


class RewardView(View):
    def get(self, request):
        return render(request, 'reward.html', {
            "big_category": 'reward'
        })


class ExchangeView(View):
    def get(self, request):
        return render(request, 'exchange.html', {
            "big_category": 'exchange'
        })


class QuestionView(View):
    def get(self, request):
        return render(request, 'question.html', {
            "big_category": 'question'
        })


class CooperationView(View):
    def get(self, request):
        return render(request, 'cooperation.html', {
            "big_category": 'cooperation'
        })


class ArticleCategoryView(View):
    def get(self, request, big_slug, category_slug):
        category = ArticleCategory.objects.get(slug=category_slug)
        all_articles = category.get_category_article()

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)  # 因为用get方法，如果get到的是空，就把1返回，所以下面的异常处理不需要考虑EmptyPage，只需处理PageNotAnInteger一场
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 10)  # Show 10 contacts per page

        all_articles = p.page(page)

        return render(request, 'categorypage.html', {
            "all_articles": all_articles,
            "category": category,
        })


class ArticleCategoryListView(ListView):
    template_name = 'categorypage.html'
    context_object_name = 'all_articles'
    paginate_by = 5

    def get_queryset(self):
        category = ArticleCategory.objects.get(slug=self.kwargs.get('category_slug'))
        return Article.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super(ArticleCategoryListView, self).get_context_data(**kwargs)
        context['category'] = ArticleCategory.objects.get(slug=self.kwargs.get('category_slug'))
        return context


class ArticleDetailView(View):
    def get(self, request, pk):
        articles = Article.objects.get(id=int(pk))
        articles.read_nums += 1
        articles.save(update_fields=['read_nums'])
        return render(request, 'article.html', {
            'article': articles
        })


class ArticleDetail(DetailView):

    template_name = 'article.html'
    context_object_name = 'article'
    model = Article

    #queryset = Article.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.read_nums += 1
        obj.save()
        return obj


class TagArticleView(View):
    def get(self, request, tag_name):
        tag = ArticleTag.objects.get(name=tag_name)
        all_articles = Article.objects.filter(tag=tag)

        return render(request, 'categorypage.html', {
            'all_articles': all_articles
        })


class TagArticleList(ListView):
    template_name = 'categorypage.html'
    context_object_name = 'all_articles'
    paginate_by = 1

    def get_queryset(self):
        tag = ArticleTag.objects.get(name=self.kwargs['tag_name'])
        return Article.objects.filter(tag=tag)

    def get_context_data(self, **kwargs):
        context = super(TagArticleList, self).get_context_data(**kwargs)
        context['tag_name'] = self.kwargs.get('tag_name')
        return context


class DateArticleView(View):
    def get(self, request, year, month):
        all_articles = Article.objects.filter(add_time__year=year, add_time__month=month)
        return render(request, 'categorypage.html', {
            'all_articles': all_articles
        })


class DateArticleList(ListView):
    template_name = 'categorypage.html'
    context_object_name = 'all_articles'

    def get_queryset(self):
        return Article.objects.filter(add_time__year=self.kwargs['year'], add_time__month=self.kwargs['month'])

    def get_context_data(self, **kwargs):
        context = super(DateArticleList, self).get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        return context



# class AddLikeView(View):
#     def post(self, request):
#         article_id = request.POST.get('article_id', '')
#         if article_id:
#             article = Article.objects.get(id=int(article_id))
#             article.like_nums += 1
#             article.save()
#             return HttpResponse('{"status":"success","msg":"您已经点过赞了"}', content_type='application/json')
#         else:
#             return HttpResponse('{"status":"fail","msg":"点赞出错了"}', content_type='application/json')


@csrf_exempt
def AddLikeView(request):
    article_id = request.POST.get('article_id', '')
    if article_id:
        article = Article.objects.get(id=int(article_id))
        article.like_nums += 1
        article.save(update_fields=['like_nums'])
        return HttpResponse('{"status":"success","msg":"您已经点过赞了"}', content_type='application/json')
    else:
        return HttpResponse('{"status":"fail","msg":"点赞出错了"}', content_type='application/json')


def page_not_found(request):
    # 全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    # 全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
