from blog.feeds import AllPostsRssFeed
from .views import AddLikeView, ArticleDetail, TagArticleList, \
    DateArticleList, IndexListView, ArticleCategoryListView, BigCategoryListView, \
    AboutView, MessageView, ResourcesView, QuestionView, RewardView, CooperationView, ExchangeView
from users.views import LogoutView, LoginView, RegisterView, ForgetPwdView
from django.views.decorators.cache import cache_page
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', IndexListView.as_view(), name="index"),
    path('category/about/', AboutView.as_view(), name="about_me"),
    path('category/message/', MessageView.as_view(), name="message"),
    path('category/resources/', ResourcesView.as_view(), name="resources"),
    path('category/reward/', RewardView.as_view(), name="reward"),
    path('category/exchange/', ExchangeView.as_view(), name="exchange"),
    path('category/question/', QuestionView.as_view(), name="question"),
    path('category/cooperation/', CooperationView.as_view(), name="cooperation"),
    path('category/<slug:big_slug>/', BigCategoryListView.as_view(), name="big_category"),
    path('category/<slug:big_slug>/<slug:category_slug>/', ArticleCategoryListView.as_view(),name="article_category"),
    path('article/<int:pk>/', ArticleDetail.as_view(), name="article_detail"),
    path('tag/<str:tag_name>/', TagArticleList.as_view(), name="tag"),
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
