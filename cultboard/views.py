from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from .forms import TeamMember

# Create your views here.


def homepage(request):
    if request.method == 'POST':
        form = TeamMember(request.POST)
        if form.is_valid():
            print('Hello')
            print(form.cleaned_data)
            return HttpResponseRedirect('/stud/gymkhana/cultural-board/')

    else:
        form = TeamMember()

    return render(request, 'homepage.html', {'form': form})


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
