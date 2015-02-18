from django.conf.urls import patterns, url
from django.views.generic.edit import CreateView
from custom_user.forms import EmailUserCreationForm
from . import views


urlpatterns = patterns('',
    url(r'^$', views.index_view),
    url(r'^admin/$', views.admin_view, name='app-admin'),
    url('^register/', CreateView.as_view(template_name='register.html', form_class=EmailUserCreationForm, success_url='/')),
    url(r'^signin/$', 'django.contrib.auth.views.login', name='app-signin', kwargs={'template_name': 'signin.html'}),
    url(r'^signout/$', 'django.contrib.auth.views.logout', name='app-signout', kwargs={'next_page': '/'}),
)
