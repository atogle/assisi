from django.conf.urls import include, url
from django.contrib import admin

import api.urls
import web.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'foo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(web.urls)),
    url(r'^api/v1/', include(api.urls)),
    url(r'^superadmin/', include(admin.site.urls)),
]
