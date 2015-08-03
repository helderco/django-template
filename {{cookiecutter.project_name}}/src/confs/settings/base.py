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

ADMINS = (
    # ('Your Name', '{{ cookiecutter.site_meail }}'),
)

MANAGERS = ADMINS

APPEND_SLASH = True


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
)

ROOT_URLCONF = 'confs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

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


# Templates

TEMPLATE_DIRS = (
    BASE_DIR.child('core', 'templates'),
)


# Email

if 'EMAIL_HOST_USER' in os.environ:
    EMAIL_USE_TLS = env('EMAIL_USE_TLS', True)
    EMAIL_HOST = env('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_PORT = env('EMAIL_PORT', 587)
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')
    DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': [],
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
