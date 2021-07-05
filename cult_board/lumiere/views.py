from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import BlogForm


# Create your views here.
# @login_required
def home(request):
    return render(request, "home.html")

class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'

class AddPostView(LoginRequiredMixin, generic.CreateView):
    model = BlogPost
    form_class = BlogForm
    template_name = 'add_post.html'
    # fields = ('title', 'content', 'author')
    # fields = '__all__'

class UpdatePostView(LoginRequiredMixin, generic.UpdateView):
    model = BlogPost
    form_class = BlogForm
    template_name = 'update_post.html'
    # fields = ['title', 'content', 'status']

class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')