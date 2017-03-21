from .models import Request, EventDistributionSiteDetails
from rest_framework import serializers, validators


def max_requests_validator(attrs):
    details = attrs['event_distribution_site_details']
    dist_site_count = Request.objects.filter(event_distribution_site_details=details).count()
    if  dist_site_count >= details.max_requests:
        raise serializers.ValidationError('No more requests can be made for %s. %d of %d requests have already been made.' %
            (details.distribution_site, dist_site_count, details.max_requests))


def dist_site_zip_match_validator(attrs):
    details = attrs['event_distribution_site_details']
    zip = attrs['zip']

    if zip not in attrs['event_distribution_site_details'].zip_codes:
        raise serializers.ValidationError('%s does not deliver to zip code %s.' % (details.distribution_site, zip))


class EventDistributionSiteDetailsSerializer(serializers.ModelSerializer):
    distribution_site = serializers.StringRelatedField()
    event = serializers.StringRelatedField()

    class Meta:
        model = EventDistributionSiteDetails
        fields = ('id', 'distribution_site', 'event', 'max_requests')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'name', 'address', 'apt', 'city', 'state', 'zip',
                  'email', 'phone', 'phone_type',
                  'phone2', 'phone_type2', 'notes', 'event_distribution_site_details')
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Request.objects.all(),
                fields=('event_distribution_site_details', 'address', 'apt', 'zip'),
                message='Someone has already made a request for this address (address, apt, and zip).'
            ),
            dist_site_zip_match_validator,
            max_requests_validator,
        ]
