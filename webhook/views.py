from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    query = request.GET.get('name')

    mode = request.GET.get('hub.mode')
    token = request.GET.get('hub.verify_token')
    challenge = request.GET.get('hub.challenge')

    if mode and token:
        if mode == 'subscribe' and token == verify_token:
            return HttpResponse('Hello, ' +   query)
        else:
            return HttpResponse('Error 2')
    else:
        return HttpResponse('Error 1')