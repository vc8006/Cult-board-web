from django.shortcuts import render
from .models import Post,Photo,Member,Achieve,Club
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

def home(request):
    return render(request,'club/home.html')
def events(request):
    return render(request,'club/events.html')
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
    }
    return render(request,'club/clubsecy.html',info)

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
    success_url= '/clubsecy'

class MemberDetailView(DetailView):
    model = Member


class MemberCreateView(CreateView):
    model = Member
    fields = ['club','name','image','position','phone_number','fb_link','insta_link','linkedin_link']

class MemberUpdateView(UpdateView):
    model = Member
    fields = ['club','name','image','position','phone_number','fb_link','insta_link','linkedin_link']

class MemberDeleteView(DeleteView):
    model = Post
    success_url= '/clubsecy'

class AchieveDetailView(DetailView):
    model = Achieve

class AchieveCreateView(CreateView):
    model = Achieve
    fields = ['club','title','image','content','date']

class AchieveUpdateView(UpdateView):
    model = Post
    fields = ['club','title','content','author']

class AchieveDeleteView(DeleteView):
    model = Post
    success_url= '/clubsecy'
class PhotoDetailView(DetailView):
    model = Photo

class PhotoCreateView(CreateView):
    model = Photo
    fields = ['club','title','image']

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['club','title','image']

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url= '/clubsecy'
