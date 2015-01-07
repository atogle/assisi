from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from nose.tools import assert_equal, assert_in, ok_
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND

from django.contrib.auth.models import User as UserAuth, AnonymousUser
from .models import Request
from .serializers import RequestSerializer
from .views import router


class AssisiApiTestCase (TestCase):
    def setUp(self):
        self.set_up()

    def tearDown(self):
        self.tear_down()

    def set_up(self):
        class URLConf:
            urlpatterns = router.urls
        self.urlconf = URLConf
        self.factory = RequestFactory()

    def tear_down(self):
        UserAuth.objects.all().delete()
        Request.objects.all().delete()

    def get_view_callback(self, name):
        for urlpattern in self.urlconf.urlpatterns:
            if urlpattern.name == name:
                return urlpattern.callback
        raise ValueError('No pattern named %r. Choices are %r' % (name, [p.name for p in self.urlconf.urlpatterns]))


class RequestDetailViewAuthenticationTests (AssisiApiTestCase):
    def init_test_assets(self, public=True):
        auth = UserAuth.objects.create_user(username='atogle', password='123')
        request = Request.objects.create(
            name='Aaron', address='123 Main St', zip='55555')

        kwargs = {'pk': request.pk}
        view = self.get_view_callback('request-detail')
        url = reverse('request-detail', kwargs=kwargs)

        return auth, request, kwargs, view, url

    def test_anonymous_cannot_GET_detail(self):
        url = self.init_test_assets()[-1]
        response = self.client.get(url)
        assert_equal(response.status_code, HTTP_403_FORBIDDEN)
