from django.conf.urls import url
from django.contrib import auth
from django.views.generic.edit import CreateView
from custom_user.forms import EmailUserCreationForm
from . import views


urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^admin/$', views.admin_view, name='app-admin'),
    url(r'^profile/$', views.profile_view, name='app-profile'),
    url(r'^register/$', CreateView.as_view(template_name='register.html', form_class=EmailUserCreationForm, success_url='/'), name='app-register'),
    url(r'^signin/$', auth.views.login, name='app-signin', kwargs={'template_name': 'signin.html'}),
    url(r'^signout/$', auth.views.logout, name='app-signout', kwargs={'next_page': '/'}),
]
