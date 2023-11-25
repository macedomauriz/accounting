from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "This is NOT admin.site.urls, this is tracker.urls, NOT the admin, this is the APP index route, generally returns tamplates"
    )


def detail(request, number):
    return HttpResponse("You're looking at question %s." % number)
