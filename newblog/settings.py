"""
Django settings for newblog project.

Generated by 'django-admin startproject' using Django 1.11.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uo6(5w@4fxacgz@d&m#pf9u9pn0xqi-2xjpt!s@5#9ngv3_f57'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # 网站地图
    'django.contrib.sitemaps', # 网站地图
    'django.contrib.humanize',  # 添加人性化过滤器
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'captcha',
    # 'DjangoUeditor',
    'social_django',
    # 'ckeditor',
    # 'ckeditor_uploader'
]

from social_django.config import PythonSocialAuthConfig

PythonSocialAuthConfig.verbose_name = 'Github用户'

AUTH_USER_MODEL = 'users.UserPro'

SITE_ID = 1

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 缓存全站
   #  'django.middleware.common.CommonMiddleware',
   #  'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'newblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'newblog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'USER': 'root',
            'PASSWORD': 'root',
            'NAME': 'blog',
            # 避免映射数据库时出现警告
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
            },
        }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
   os.path.join(BASE_DIR,'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = 'article/'

EMAIL_HOST = "smtp.163.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "这里应该是你的163邮箱"
EMAIL_HOST_PASSWORD = "这里应该是你的邮箱密码"
EMAIL_USE_TLS = False
EMAIL_FROM = "这里应该是你的163邮箱"
# STATIC_ROOT = os.path.join(BASE_DIR,'static/')


SITE_DESCRIPTION = "KenZhang的个人博客，记录生活的瞬间，分享学习的心得，感悟生活，留住感动，静静寻觅生活的美好"

SITE_KEYWORDS = "KenZhang,网络,爬虫,IT,技术,博客,Python,Django"

NOTICE = "人生苦短，必用Python"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 60 * 60 * 12,
    }
}

# CACHE_MIDDLEWARE_SECONDS= 60 * 60 * 12

AUTHENTICATION_BACKENDS = (
    #'social_core.backends.qq.QQOAuth2',
    #'social_core.backends.weixin.WeixinOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_URL_NAMESPACE = 'social' # 新增

# 填写Github中获取到的KEY和SECRET

SOCIAL_AUTH_GITHUB_KEY = '你的Client ID'
SOCIAL_AUTH_GITHUB_SECRET = '你的Client Secret'
SOCIAL_AUTH_GITHUB_USE_OPENID_AS_USERNAME = True

# 登陆成功后的回调路由
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/' # 登陆成功之后的路由，可以自定义要返回到那个页面，此处返回到首页


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
                    ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
                    ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat', '-', 'Maximize',
                     'ShowBlocks', '-', 'Subscript', 'Superscript', 'Markdown'],
                    ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                     'HiddenField'],
                    ['Bold', 'Italic', 'Underline', 'Strike', '-'],
                    ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
                    ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                    ['Link', 'Unlink', 'Anchor'],
                    ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
                    ['Styles', 'Format', 'Font', 'FontSize'],
                    ['TextColor', 'BGColor', 'CodeSnippet'],

                    ),
        'extraPlugins': ['codesnippet','markdown'],
    }
}

SIMPLEUI_LOGO = 'http://img.0a0z.cn/BlogPhoto/20200105133312.png'
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False