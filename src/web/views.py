from django.shortcuts import render_to_response


def index_view(request):
    return render_to_response('index.html')
