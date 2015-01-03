from django.db import models


class Request(models.Model):
    name = models.CharField(null=True, blank=True, max_length=60)
    address = models.CharField(null=True, blank=True, max_length=200)
    zip = models.CharField(null=True, blank=True, max_length=200)
    email = models.CharField(null=True, blank=True, max_length=200)
    home_phone = models.CharField(null=True, blank=True, max_length=20)
    mobile_phone = models.CharField(null=True, blank=True, max_length=20)
