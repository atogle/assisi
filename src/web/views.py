from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect


def index_view(request):
    return redirect('app-admin')


@login_required
def admin_view(request):
    return render_to_response('admin.html')
