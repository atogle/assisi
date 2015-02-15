from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from project import assisi_config


def index_view(request):
    return redirect('app-admin')


@login_required
def admin_view(request):
    config_yml = assisi_config.get_config('../project/config.yml')
    context = {
        'distribution_sites': config_yml['distribution_sites']
    }

    return render(request, 'admin.html', context)
