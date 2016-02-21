from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from api import models
from .forms import SingleEventDistributionSiteDetailForm


def index_view(request):
    # User is already assigned to an event/distribution site. Get to work!
    if hasattr(request.user, 'eventdistributionsitedetails_set') and request.user.eventdistributionsitedetails_set.filter(event__active__exact=True).count() > 0:
        return redirect('app-admin')
    else:
        return redirect('app-profile')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = SingleEventDistributionSiteDetailForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['event_distribution_site_details']
            request.user.eventdistributionsitedetails_set.add(id)
            return redirect('app-admin')
    else:
        form = SingleEventDistributionSiteDetailForm()

    events = {}
    event = ''
    distribution_sites = None
    for details in models.EventDistributionSiteDetails.objects.filter(event__active__exact=True):
        if events.get(details.event.name, None) is None:
            events[details.event.name] = []

        events[details.event.name].append({
            'id': details.id,
            'name': details.distribution_site.name
        })

    if len(events.values()) > 0:
        distribution_sites = next(iter(events.values()))
        event = next(iter(events.keys()))

    context = {
        # Only use the first event. The UI doesn't currently support multiple events.
        'distribution_sites': distribution_sites,
        'event': event,
        'form': form,
        'selected_distribution_site': None if not hasattr(request.user, 'eventdistributionsitedetails_set') else request.user.eventdistributionsitedetails_set.filter(event__active__exact=True).first()
    }

    return render(request, 'profile.html', context)


@login_required
def admin_view(request):
    events = {}
    distribution_sites = None
    for details in request.user.eventdistributionsitedetails_set.filter(event__active__exact=True):
        if events.get(details.event.name, None) is None:
            events[details.event.name] = []

        events[details.event.name].append({
            'id': details.id,
            'name': details.distribution_site.name,
            'max_requests': details.max_requests,
            'zip_codes': details.zip_codes
        })

    if len(events.values()) > 0:
        distribution_sites = next(iter(events.values()))
    else:
        # User has not been assigned to an event/distribution site.
        return redirect('app-profile')

    context = {
        # Only use the first event. The UI doesn't currently support multiple events.
        'distribution_sites': distribution_sites
    }

    return render(request, 'admin.html', context)
