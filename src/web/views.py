from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import json
import os
import yaml


def get_config(filename):
    config_file = open(filename)
    try:
        config_yml = yaml.load(config_file)
    finally:
        config_file.close()

    return config_yml


def index_view(request):
    return redirect('app-admin')


@login_required
def admin_view(request):
    path = os.path.abspath(os.path.dirname(__file__))
    fileepath = os.path.join(path, 'config.yml')
    config_yml = get_config(fileepath)
    context = {
        'partners': config_yml['partners']
    }

    return render(request, 'admin.html', context)
