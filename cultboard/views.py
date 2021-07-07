from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from .models import Club
# from .forms import teamMember

# Create your views here.


def homepage(request):
    # if request.method == 'POST':
    #     form1 = teamMember(request.POST)
    #     if form1.is_valid():
    #         form1.save()
    #         print(form1.cleaned_data)
    #         return HttpResponseRedirect('/stud/gymkhana/cultural-board/')
    # else:
    #     form1 = teamMember()
    return render(request, 'cultboard/homepage.html')


def clubs(request):
    list = {
        'clubs' : Club.objects.all(),
    }
    return render(request, 'cultboard/clubs.html',list)


def majorEvents(request):
    return render(request, 'cultboard/majorEvents.html')


def upcomingEvents(request):
    return render(request, 'cultboard/upcomingEvents.html')


def services(request):
    return render(request, 'cultboard/services.html')


def aboutUs(request):
    return render(request, 'cultboard/aboutUs.html')
