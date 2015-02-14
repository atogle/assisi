from .models import Request
from rest_framework import serializers, validators


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'name', 'address', 'apt', 'city', 'state', 'zip',
                  'distribution_site', 'email', 'phone', 'phone_type')
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Request.objects.all(),
                fields=('address', 'apt', 'zip'),
                message='Someone has already made a request for this address (address, apt, and zip).'
            )
        ]
