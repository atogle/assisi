from django.contrib import admin
from .models import DistributionSite, Event, EventDistributionSiteDetails, Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'apt', 'zip', 'event_distribution_site_details')


@admin.register(EventDistributionSiteDetails)
class EventDistributionSiteDetailsAdmin(admin.ModelAdmin):
    list_display = ('event', 'distribution_site', 'request_count', 'max_requests', 'zip_codes', 'user_count')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


@admin.register(DistributionSite)
class DistributionSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')
