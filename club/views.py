from django.shortcuts import render
from .models import Post,Photo,Member
# Create your views here.

def home(request):
    return render(request,'club/home.html')
def events(request):
    return render(request,'club/events.html')
def gallery(request):
    appear= {
        'photos':Photo.objects.all(),
    }
    return render(request,'club/gallery.html')
def blog(request):
    content= {
        'posts': Post.objects.all(),
    }
    return render(request,'club/blog.html',content)
def achieve(request):
    return render(request,'club/achievements.html')
def team(request):
    context = {
        'members': Member.objects.all(),
    }
    return render(request,'club/team.html',context)
