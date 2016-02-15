from .models import Request
from rest_framework import viewsets, routers, permissions, filters
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_jsonp.renderers import JSONPRenderer
from .renderers import PaginatedCSVRenderer
from .serializers import RequestSerializer


class IsAuthenticatedOrWriteOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a write-only request.
    """

    def has_permission(self, request, view):
        safe_methods = ['POST', 'HEAD', 'OPTIONS']

        if (request.method in safe_methods or
            request.user and
            request.user.is_authenticated()):
            return True
        return False


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    renderer_classes = (JSONRenderer, JSONPRenderer, BrowsableAPIRenderer, PaginatedCSVRenderer)
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticatedOrWriteOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('distribution_site',)

    def get_queryset(self):
        # Return only requests relevant to the current user.
        ids = self.request.user.eventdistributionsitedetails_set.all().values_list('id', flat=True)
        return Request.objects.filter(event_distribution_site_details__pk__in=ids)

router = routers.DefaultRouter()
router.register('requests', RequestViewSet, 'request')
