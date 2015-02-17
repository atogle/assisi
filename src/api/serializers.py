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
        raise serializers.ValidationError('We are not delivering to zip code %s.' % zip)


def max_requests_validator(attrs):
    dist_site_name = attrs['distribution_site']
    dist_site_config = next((c for c in config['distribution_sites'] if c['name'] == dist_site_name), None)

    if dist_site_config == None:
        raise serializers.ValidationError('Unknown distribution site named %s.' % dist_site_name)

    dist_site_max = dist_site_config['max']
    dist_site_count = Request.objects.filter(distribution_site=dist_site_name).count()
    if  dist_site_count >= dist_site_max:
        raise serializers.ValidationError('No more requests can be made for %s. %d of %d requests have already been made.' %
            (dist_site_name, dist_site_count, dist_site_max))


def dist_site_zip_match_validator(attrs):
    zip = attrs['zip']
    dist_site_name = attrs['distribution_site']
    dist_site_config = next((c for c in config['distribution_sites'] if c['name'] == dist_site_name), None)

    if zip not in dist_site_config['zips']:
        raise serializers.ValidationError('%s does not deliver to zip code %s.' % (dist_site_name, zip))


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'name', 'address', 'apt', 'city', 'state', 'zip',
                  'distribution_site', 'email', 'phone', 'phone_type', 'notes')
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Request.objects.all(),
                fields=('address', 'apt', 'zip'),
                message='Someone has already made a request for this address (address, apt, and zip).'
            ),
            zip_code_validator,
            max_requests_validator,
            dist_site_zip_match_validator
        ]
