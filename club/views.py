from django.shortcuts import render
from django.urls import reverse
from .models import BlogPost,Photo,Achieve,Club, WelcomeNote,Events
from cultboard.models import TeamMember
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


#  clubs views
def home(request):
    welcome_note = WelcomeNote.objects.all()
    return render(request,'club/home.html',{'welcome_note': welcome_note})

def main_page(request):
    days = 7*3
    # start_date = date.today()
    start_date = datetime.now()
    end_date = start_date + timedelta(days=days)
    events = Events.objects.filter(expired_date__range=[start_date, end_date])
    # events=Events.objects.all()
    return render(request,'club/main_page.html',{'events':events})

def events(request):
    events= Events.objects.all()
    return render(request,'club/events.html',{'events':events})

def gallery(request):
    appear= {
        'photos':Photo.objects.all(),
    }
    return render(request,'club/gallery.html',appear)

def blog(request):
    content= {
        'posts': BlogPost.objects.filter(status=1).order_by('-created_on'),
    }
    return render(request,'club/blog.html',content)

def achieve(request):
    list = {
        'achievements' : Achieve.objects.all(),
    }
    return render(request,'club/achievements.html',list)


def team(request):
    context = {
        'members': TeamMember.objects.all(),
    }
    return render(request,'club/team.html',context)

def clubsecy(request):
    info = {
        'photos':Photo.objects.all(),
        'posts': BlogPost.objects.filter(status=1).order_by('-created_on'),
        'achievements' : Achieve.objects.all(),
        'members': TeamMember.objects.all(),
        'events':Events.objects.all(),
        'welcome_note':WelcomeNote.objects.all()
    }
    return render(request,'club/clubsecy.html',info)


# blog views
class BlogDetailView(DetailView):
    model = BlogPost

class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['club','title','author','content','status']

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['club','title','author','content','status']

class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url= '/stud/gymkhana/CulturalBoard/Club/clubsecy'


class EventDetailView(DetailView):
    model = Events

class EventCreateView(CreateView):
    model = Events
    fields = ['club','title','content','expired_date']

class EventUpdateView(UpdateView):
    model = Events
    fields = ['club','title','content','expired_date']

class EventDeleteView(DeleteView):
    model = Events
    success_url= '/stud/gymkhana/CulturalBoard/Club/clubsecy'


class MemberDetailView(DetailView):
    model = TeamMember

class MemberCreateView(CreateView):
    model = TeamMember
    fields = ['club','name','image','position','phone_number','fb_link','insta_link','linkedin_link']

class MemberUpdateView(UpdateView):
    model = TeamMember
    fields = ['club','name','image','position','phone_number','fb_link','insta_link','linkedin_link']

class MemberDeleteView(DeleteView):
    model = TeamMember
    success_url= '/stud/gymkhana/CulturalBoard/Club/clubsecy'

class AchieveDetailView(DetailView):
    model = Achieve

class AchieveCreateView(CreateView):
    model = Achieve
    fields = ['club','title','image','content','date']

class AchieveUpdateView(UpdateView):
    model = Achieve
    fields = ['club','title','image','content','date']

class AchieveDeleteView(DeleteView):
    model = Achieve
    success_url= '/stud/gymkhana/CulturalBoard/Club/clubsecy'

class PhotoDetailView(DetailView):
    model = Photo

class PhotoCreateView(CreateView):
    model = Photo
    fields = ['club','title','image']

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['club','title','image',]

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url= '/stud/gymkhana/CulturalBoard/Club/clubsecy'


class WelcomeUpdateView(UpdateView):
    model = WelcomeNote
    fields = ['content']

class WelcomeDetailView(DetailView):
    model = WelcomeNote
