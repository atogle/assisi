from django.db import models


class Request(models.Model):
    name = models.CharField(null=True, blank=True, max_length=60)
    address = models.CharField(null=True, blank=True, max_length=200)
    apt = models.CharField(null=True, blank=True, max_length=200)
    city = models.CharField(null=True, blank=True, max_length=200)
    state = models.CharField(null=True, blank=True, max_length=200)
    zip = models.CharField(null=True, blank=True, max_length=200)
    distribution_site = models.CharField(null=True, blank=True, max_length=200)
    email = models.CharField(null=True, blank=True, max_length=200)
    phone = models.CharField(null=True, blank=True, max_length=20)
    phone_type = models.CharField(null=True, blank=True, max_length=20)
