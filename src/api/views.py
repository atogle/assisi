from .models import Request
from rest_framework import viewsets, routers, permissions
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
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticatedOrWriteOnly,)

router = routers.DefaultRouter()
router.register('requests', RequestViewSet)
