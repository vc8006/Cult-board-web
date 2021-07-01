from django.shortcuts import render
from django.urls import reverse 
from .models import Post,Photo,Member,Achieve,Club, WelcomeNote,Events
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
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
    start_date = date.today()
    end_date = start_date + timedelta(days=days)
    events = Events.objects.filter(expired_date__range=[start_date, end_date])
    return render(request,'club/main_page.html',{'events':events})

def events(request):
    events=Events.objects.all()
    return render(request,'club/events.html',{'events':events})

def gallery(request):
    appear= {
        'photos':Photo.objects.all(),
    }
    return render(request,'club/gallery.html',appear)

def blog(request):
    content= {
        'posts': Post.objects.all(),
    }
    return render(request,'club/blog.html',content)

def achieve(request):
    list = {
        'achievements' : Achieve.objects.all(),
    }
    return render(request,'club/achievements.html',list)


def team(request):
    context = {
        'members': Member.objects.all(),
    }
    return render(request,'club/team.html',context)

def clubsecy(request):
    info = {
        'photos':Photo.objects.all(),
        'posts': Post.objects.all(),
        'achievements' : Achieve.objects.all(),
        'members': Member.objects.all(),
        'events':Events.objects.all(),
        'welcome_note':WelcomeNote.objects.all()
    }
    return render(request,'club/clubsecy.html',info)


# blog views
class BlogDetailView(DetailView):
    model = Post

class BlogCreateView(CreateView):
    model = Post
    fields = ['club','title','content','author']

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['club','title','content','author']

class BlogDeleteView(DeleteView):
    model = Post
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
    model = Member

class MemberCreateView(CreateView):
    model = Member
    fields = ['club','name','image','position','phone_number','fb_link','insta_link','linkedin_link']

class MemberUpdateView(UpdateView):
    model = Member
    fields = ['club','name','image','position','phone_number','fb_link','insta_link','linkedin_link']

class MemberDeleteView(DeleteView):
    model = Member
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
    
