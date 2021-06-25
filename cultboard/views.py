from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def homepage(request):
    return render(request, 'cultboard/homepage.html')


def clubs(request):
    return render(request, 'cultboard/clubs.html')


def majorEvents(request):
    return render(request, 'cultboard/majorEvents.html')


def upcomingEvents(request):
    return render(request, 'cultboard/upcomingEvents.html')


def services(request):
    return render(request, 'cultboard/services.html')


def aboutUs(request):
    return render(request, 'cultboard/aboutUs.html')