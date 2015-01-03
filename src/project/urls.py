from django.conf.urls import patterns, include, url
from django.contrib import admin

import api.urls
import web.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include(web.urls)),
    url(r'^api/v1/', include(api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
