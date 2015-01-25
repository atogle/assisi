from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.index_view),
    url(r'^admin/$', views.admin_view, name='app-admin'),
    url(r'^signin/$', 'django.contrib.auth.views.login', name='app-signin', kwargs={'template_name': 'signin.html'}),
    url(r'^signout/$', 'django.contrib.auth.views.logout', name='app-signout', kwargs={'next_page': '/'}),
)
