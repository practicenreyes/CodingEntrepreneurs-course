from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'joins.views.home', name='home'),
    url(r'^(?P<ref_id>\d+)$', 'joins.views.share', name='share'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
