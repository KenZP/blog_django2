# from django.conf.urls import url

from blog.feeds import AllPostsRssFeed
from .views import IndexView, BigCategoryView, ArticleCategoryView, ArticleDetailView, \
    TagArticleView, DateArticleView, AddLikeView, ArticleDetail, TagArticleList, \
    DateArticleList, IndexListView, ArticleCategoryListView  # MessageView
from users.views import LogoutView, LoginView, RegisterView, ForgetPwdView
from django.views.decorators.cache import cache_page
from django.urls import path, re_path, include

# urlpatterns = [
#     url(r'^$', cache_page(5)(IndexView.as_view()), name="index"),
#     # url(r'^category/(?P<big_slug>.*?)/$', BigCategoryView.as_view(), name="big_category"),
#     url(r'^category/(?P<big_slug>[^/]+)/$', cache_page(10)(BigCategoryView.as_view()), name="big_category"),
#     url(r'^category/(?P<big_slug>[^/]+)/(?P<category_slug>[^/]+)/$', cache_page(10)(ArticleCategoryView.as_view()), name="article_category"),
#     url(r'^article/(?P<article_id>\d+)/$', cache_page(10)(ArticleDetailView.as_view()), name="article_detail"),
#     url(r'^tag/(?P<tag_name>[^/]+)/$', TagArticleView.as_view(), name="tag"),
#     url(r'^date/(?P<year>\d+)/(?P<month>\d+)/$', DateArticleView.as_view(), name="date"),
#     url(r'^logout/$', LogoutView.as_view(), name="logout"),
#     url(r'^login/$', LoginView.as_view(), name="login"),
#     url(r'^register/$', RegisterView.as_view(), name="register"),
#     url(r'^add_like/$', AddLikeView, name="add_like"),
#     url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
#     # url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
#     # url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
#     # url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
#     # url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
# ]
app_name = 'blog'
urlpatterns = [
    path('', IndexListView.as_view(), name="index"),
    # url(r'^category/(?P<big_slug>.*?)/$', BigCategoryView.as_view(), name="big_category"),
    #re_path(r'^category/(?P<big_slug>[^/]+)/$', BigCategoryView.as_view(), name="big_category"),
    path('category/<slug:big_slug>/', BigCategoryView.as_view(), name="big_category"),
    #re_path(r'^category/(?P<big_slug>[^/]+)/(?P<category_slug>[^/]+)/$', ArticleCategoryView.as_view(), name="article_category"),
    path('category/<slug:big_slug>/<slug:category_slug>/', ArticleCategoryListView.as_view(),name="article_category"),
    #re_path(r'^article/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name="article_detail"),
    path('article/<int:pk>/', ArticleDetail.as_view(), name="article_detail"),
    #re_path(r'^tag/(?P<tag_name>[^/]+)/$', TagArticleView.as_view(), name="tag"),
    path('tag/<str:tag_name>/', TagArticleList.as_view(), name="tag"),
    #re_path(r'^date/(?P<year>\d+)/(?P<month>\d+)/$', DateArticleView.as_view(), name="date"),
    path('date/<int:year>/<int:month>/', DateArticleList.as_view(), name="date"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('add_like/', AddLikeView, name="add_like"),
    path('forget/', ForgetPwdView.as_view(), name="forget_pwd"),
    # url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    # url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    # url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    # url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
# 记得在顶部引入 AllPostsRssFeed
    path('all/rss/', AllPostsRssFeed(), name='rss'),
]
