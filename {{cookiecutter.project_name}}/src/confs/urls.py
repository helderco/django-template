# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
{%- if cookiecutter.django_cms == 'yes' %}

from cms.sitemaps import CMSSitemap
{%- endif %}


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    {%- if cookiecutter.django_cms == 'yes' %}
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),
    {%- endif %}
]

# This is only needed when using runserver.
if settings.DEBUG:
    from django.views import defaults
    urlpatterns = [
      url(r'^500/$', defaults.server_error),
      url(r'^403/$', defaults.permission_denied),
      url(r'^404/$', defaults.page_not_found),
    ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
