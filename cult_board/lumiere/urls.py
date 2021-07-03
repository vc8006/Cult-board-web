from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.PostList.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='blogpost_detail'),
    path('blog/add_post', views.AddPostView.as_view(), name='add_post'),
    path('blog/update_post/<slug:slug>', views.UpdatePostView.as_view(), name='update_post'),
    path('blog/<slug:slug>/delete_post', views.DeletePostView.as_view(), name='delete_post'),
]