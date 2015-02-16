from .models import Request
from rest_framework import serializers, validators
from project import assisi_config


config = assisi_config.get_config('../project/config.yml')


def zip_code_validator(attrs):
    # pluck zip code lists from the config
    zips = [sites['zips'] for sites in config['distribution_sites']]
    # flatten the list
    zips = sum(zips, [])
    zip = attrs['zip']

    if zip not in zips:
        raise serializers.ValidationError('We are not delivering to this zip code.')


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
            ),
            zip_code_validator
        ]
