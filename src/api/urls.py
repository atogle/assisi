from django.conf.urls import include, url
from .views import router


urlpatterns = [
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^', include('rest_framework.urls',
                               namespace='rest_framework')),
]
