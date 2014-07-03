from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

# use i18n_patterns for internationalized urls
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
