from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index_view(request):
    return redirect('app-admin')


@login_required
def admin_view(request):
    events = {}
    for details in request.user.eventdistributionsitedetails_set.filter(event__active__exact=True):
        if events.get(details.event.name, None) is None:
            events[details.event.name] = []

        events[details.event.name].append({
            'id': details.id,
            'name': details.distribution_site.name,
            'max_requests': details.max_requests,
            'zip_codes': details.zip_codes
        })

    context = {
        # Only use the first event. The UI doesn't currently support multiple events.
        'distribution_sites': next(iter(events.values()))
    }

    return render(request, 'admin.html', context)
