from .models import Request
from rest_framework import serializers


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'name', 'address', 'zip', 'email', 'phone',
                  'phone_type')
