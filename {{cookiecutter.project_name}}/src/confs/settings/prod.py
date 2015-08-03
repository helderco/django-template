# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import *


DEBUG = False

# Allow all host headers
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
)

# Sentry?
try:
    import raven.contrib.django.raven_compat
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)

    if 'SENTRY_DSN' in os.environ:
        RAVEN_CONFIG = {
            'dsn': os.environ['SENTRY_DSN']
        }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }

except ImportError:
    pass
