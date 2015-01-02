from .models import Request
from rest_framework import serializers


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'first_name', 'last_name', 'address', 'city', 'state',
                  'zip', 'email', 'home_phone', 'mobile_phone')
