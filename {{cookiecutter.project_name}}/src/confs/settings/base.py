# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Django settings.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os

import dj_database_url
from getenv import env
from unipath import Path


BASE_DIR = Path(__file__).absolute().ancestor(3)

gettext = lambda s: s


SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

ADMINS = (
    ('Webmaster', '{{ cookiecutter.site_email|default('webmaster@localhost') }}'),
)


# Application definition

INSTALLED_APPS = (
    # Core
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    {%- if cookiecutter.django_cms == 'yes' %}

    # Admin
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.redirects',

    # Core django-cms (do not sort this group)
    'django.contrib.sites',
    'djangocms_text_ckeditor',  # note this needs to be before the 'cms' entry
    'cms',  # django CMS itself
    'treebeard',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for javascript and css management

    # Other third party
    'ckeditor',
    'filer',
    'easy_thumbnails',

    # Plugins
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    # 'djangocms_flash',
    # 'djangocms_googlemap',
    # 'djangocms_inherit',
    # 'djangocms_link',
    {%- else %}
    'django.contrib.admin',
    {%- endif %}

    # Custom apps
    # 'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    {%- if cookiecutter.django_cms == 'yes' %}
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    {%- endif %}
)


# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('core', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                {%- if cookiecutter.django_cms == 'yes' %}
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                {%- endif %}
            ],
        },
    },
]


# Application definition

ROOT_URLCONF = 'confs.urls'
WSGI_APPLICATION = 'confs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    # URL schema: https://github.com/kennethreitz/dj-database-url#url-schema
    'default': dj_database_url.config(),
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pt'

TIME_ZONE = 'Atlantic/Azores'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
    BASE_DIR.child('core', 'static'),
)

STATIC_ROOT = BASE_DIR.parent.child('public', 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR.parent.child('public', 'media')
MEDIA_URL = '/media/'


{% if cookiecutter.django_cms == 'yes' -%}
# Django CMS

LANGUAGES = (
    ## Customize this
    ('pt', gettext('pt')),
)

CMS_TEMPLATES = (
    ## Customize this
    ('base.html', 'Default site page'),
)

MIGRATION_MODULES = {
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_utils': 'cmsplugin_filer_utils.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}


# Thumbnails

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


# CkEditor

CKEDITOR_UPLOAD_PATH = MEDIA_ROOT


{% endif -%}

{% if cookiecutter.redis == 'yes' -%}
# Redis caching

if 'REDIS_BACKEND' in os.environ:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": env('REDIS_BACKEND'),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "IGNORE_EXCEPTIONS": True,
            }
        }
    }

    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"


{% endif -%}

# Email

{% if cookiecutter.site_email -%}
DEFAULT_FROM_EMAIL = '{{ cookiecutter.site_email }}'
{% endif -%}
EMAIL_USE_TLS = env('EMAIL_USE_TLS', True)
EMAIL_HOST = env('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = env('EMAIL_PORT', 587)
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
