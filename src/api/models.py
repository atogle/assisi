from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class TimeStampedModel (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DistributionSite(TimeStampedModel):
    name = models.CharField(null=True, blank=True, max_length=60)
    address = models.CharField(null=True, blank=True, max_length=200)
    apt = models.CharField(null=True, blank=True, max_length=200)
    city = models.CharField(null=True, blank=True, max_length=200)
    state = models.CharField(null=True, blank=True, max_length=200)
    zip = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Distribution Site'
        verbose_name_plural = 'Distribution Sites'


class Event(TimeStampedModel):
    name = models.CharField(null=True, blank=True, max_length=60)
    active = models.BooleanField()
    distribution_sites = models.ManyToManyField(DistributionSite, through='EventDistributionSiteDetails')

    def __str__(self):
        return self.name


class EventDistributionSiteDetails(TimeStampedModel):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    distribution_site = models.ForeignKey(DistributionSite, on_delete=models.SET_NULL, null=True)
    max_requests = models.IntegerField(null=True)
    zip_codes = ArrayField(
        models.CharField(max_length=5),
        null=True
    )
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def request_count(self):
        return self.request_set.count()

    def user_count(self):
        return self.users.count()

    def __str__(self):
        return '[No Event]' if self.event is None else self.event.name + ': ' + '[No Distribution Site]' if self.distribution_site is None else self.distribution_site.name

    class Meta:
        verbose_name = 'Event Distribution Site Details'
        verbose_name_plural = 'Event Distribution Site Details'


class Request(TimeStampedModel):
    PHONE_CHOICES = (
        ('Home', 'Home'),
        ('Mobile', 'Mobile')
    )

    event_distribution_site_details = models.ForeignKey(EventDistributionSiteDetails, null=True, on_delete=models.SET_NULL)

    name = models.CharField(null=True, blank=True, max_length=60)
    address = models.CharField(null=True, blank=True, max_length=200)
    apt = models.CharField(null=True, blank=True, max_length=200)
    city = models.CharField(null=True, blank=True, max_length=200)
    state = models.CharField(null=True, blank=True, max_length=200)
    zip = models.CharField(null=True, blank=True, max_length=200)
    distribution_site = models.CharField(null=True, blank=True, max_length=200)
    email = models.CharField(null=True, blank=True, max_length=200)
    phone = models.CharField(null=True, blank=True, max_length=20)
    phone_type = models.CharField(null=True, blank=True, max_length=20, choices=PHONE_CHOICES)
    phone2 = models.CharField(null=True, blank=True, max_length=20)
    phone_type2 = models.CharField(null=True, blank=True, max_length=20, choices=PHONE_CHOICES)
    notes = models.CharField(null=True, blank=True, max_length=1024)

    def __str__(self):
        return self.address
