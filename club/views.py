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
def home(request,club_name):
    welcome_note = WelcomeNote.objects.all()
    return render(request,'club/home.html',{'welcome_note': welcome_note,'club_name':club_name})

# def main_page(request):
#     days = 7*3
#     start_date = datetime.now()
#     end_date = start_date + timedelta(days=days)
#     events = Events.objects.filter(expired_date__range=[start_date, end_date])
#     return render(request,'club/main_page.html',{'events':events})

def events(request,club_name):
    events=Events.objects.filter(club__name=club_name)
    return render(request,'club/events.html',{'events':events,'club_name':club_name})

def gallery(request,club_name):
    appear= {
        'photos':Photo.objects.filter(club__name=club_name),
        'club_name':club_name
    }
    return render(request,'club/gallery.html',appear)

def blog(request,club_name):
    content= {
        'posts': BlogPost.objects.filter(club__name=club_name,status=1).order_by('-created_on'),
        'club_name':club_name
    }
    return render(request,'club/blog.html',content)

def achieve(request,club_name):
    list = {
        'achievements' : Achieve.objects.filter(club__name=club_name),
        'club_name':club_name,
    }
    return render(request,'club/achievements.html',list)


def team(request,club_name):
    context = {
        'members': TeamMember.objects.filter(club__name=club_name),
        'club_name':club_name
    }
    return render(request,'club/team.html',context)

def clubsecy(request,club_name):
    info = {
        'photos':Photo.objects.filter(club__name=club_name),
        'posts': BlogPost.objects.filter(status=1,club__name=club_name).order_by('-created_on'),
        'achievements' : Achieve.objects.filter(club__name=club_name),
        'members': TeamMember.objects.filter(club__name=club_name),
        'events':Events.objects.filter(club__name=club_name),
        'welcome_note':WelcomeNote.objects.all(),
        'club_name':club_name
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

# def AchieveUpdateView(request,club_name,pk):
#     return render(request,'club/achieve_form.html',{'club_name':club_name, 'pk':pk})

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
