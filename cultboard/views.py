from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from .models import Club, Detail, UpcomingEvent,MajorEvent,TeamMember,Note
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from club.models import Events, WelcomeNote
import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
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
    welcome_note = Note.objects.all()
    gensec = Detail.objects.all()
    return render(request, 'cultboard/homepage.html',{'welcome_note':welcome_note, 'gensec':gensec})


def clubs(request):
    list = {
        'clubs' : Club.objects.all(),
    }
    return render(request, 'cultboard/clubs.html',list)


def majorEvents(request):
    major_events = MajorEvent.objects.all()
    return render(request, 'cultboard/majorEvents.html',{'major_events':major_events})


def upcomingEvents(request):
    days = 7*3
    start_date = datetime.now()
    end_date = start_date + timedelta(days=days)
    events = Events.objects.filter(expired_date__range=[start_date, end_date])
    return render(request, 'cultboard/upcomingEvents.html',{'events':events})


def services(request):
    return render(request, 'cultboard/services.html')


def aboutUs(request):
    return render(request, 'cultboard/aboutUs.html')

def gensec(request):
    info = {
        'upcoming_events':UpcomingEvent.objects.all(),
        'major_events': MajorEvent.objects.all(),
        'members': TeamMember.objects.all(),
        'notes':Note.objects.all(),
        'gensec':Detail.objects.all()
    }
    return render(request,'cultboard/gensec.html',info)


class MajorEventCreateView(CreateView):
    model = MajorEvent
    fields = ['name','logo','description','gallary_event','fb_link','insta_link','linkedin_link']

class MajorEventDetailView(DetailView):
    model = MajorEvent

class MajorEventUpdateView(UpdateView):
    model = MajorEvent
    fields = ['name','logo','description','gallary_event','fb_link','insta_link','linkedin_link']

class MajorEventDeleteView(DeleteView):
    model = MajorEvent
    success_url= '/stud/gymkhana/CulturalBoard/gensec'



class UpcomingEventCreateView(CreateView):
    model = UpcomingEvent
    fields = ['name','logo','description']

class UpcomingEventDetailView(DetailView):
    model = UpcomingEvent

class UpcomingEventUpdateView(UpdateView):
    model = UpcomingEvent
    fields = ['name','logo','description']

class UpcomingEventDeleteView(DeleteView):
    model = UpcomingEvent
    success_url= '/stud/gymkhana/CulturalBoard/gensec'



class MemberCreateView(CreateView):
    model = TeamMember
    fields = ['club','name','image','position','phone_number','fb_link','insta_link','linkedin_link']

class MemberDetailView(DetailView):
    model = TeamMember

class MemberUpdateView(UpdateView):
    model = TeamMember
    fields = ['club','name','image','position','phone_number','fb_link','insta_link','linkedin_link']

class MemberDeleteView(DeleteView):
    model = TeamMember
    success_url= '/stud/gymkhana/CulturalBoard/gensec'



class NoteDetailView(DetailView):
    model = Note

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title','note']

class NoteDeleteView(DeleteView):
    model = Note
    success_url= '/stud/gymkhana/CulturalBoard/gensec'


class GensecCreateView(CreateView):
    model = Detail
    fields = ['name','image','position','info','phone_number','email']

class GensecDetailView(DetailView):
    model = Detail

class GensecUpdateView(UpdateView):
    model = Detail
    fields = ['name','image','position','info','phone_number','email']

class GensecDeleteView(DeleteView):
    model = Detail
    success_url= '/stud/gymkhana/CulturalBoard/gensec'