from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


def index_view(request):
    return render_to_response('index.html')


@login_required
def admin_view(request):
    return render_to_response('admin.html')
