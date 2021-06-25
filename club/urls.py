from django.urls import path
from . import views
from .views import BlogDetailView,MemberDetailView,AchieveDetailView,PhotoDetailView
from .views import BlogCreateView,MemberCreateView,AchieveCreateView,PhotoCreateView
from .views import BlogUpdateView,MemberUpdateView,AchieveUpdateView,PhotoUpdateView
from .views import BlogDeleteView,MemberDeleteView,AchieveDeleteView,PhotoDeleteView

urlpatterns = [
    path('',views.home,name='club-home'),
    path('events/',views.events,name='club-events'),
    path('gallery/',views.gallery,name='club-gallery'),
    path('gallery/<int:pk>',PhotoDetailView.as_view(),name='photo-detail'),
    path('gallery/new',PhotoCreateView.as_view(),name='photo-create'),
    path('gallery/<int:pk>/update',PhotoUpdateView.as_view(),name='photo-update'),
    path('gallery/<int:pk>/delete',PhotoDeleteView.as_view(),name='photo-delete'),
    path('blog/',views.blog,name='club-blogs'),
    path('blog/<int:pk>',BlogDetailView.as_view(),name='blog-detail'),
    path('blog/new',BlogCreateView.as_view(),name='blog-create'),
    path('blog/<int:pk>/update',BlogUpdateView.as_view(),name='blog-update'),
    path('blog/<int:pk>/delete',BlogDeleteView.as_view(),name='blog-delete'),
    path('achievements/',views.achieve,name='club-achieve'),
    path('achievements/<int:pk>',AchieveDetailView.as_view(),name='achieve-detail'),
    path('achievements/new',AchieveCreateView.as_view(),name='achieve-create'),
    path('achievements/<int:pk>/update',AchieveUpdateView.as_view(),name='achieve-update'),
    path('achievements/<int:pk>/delete',AchieveDeleteView.as_view(),name='achieve-delete'),
    path('team/',views.team,name='club-team'),
    path('team/<int:pk>',MemberDetailView.as_view(),name='member-detail'),
    path('team/new',MemberCreateView.as_view(),name='member-create'),
    path('team/<int:pk>/update',MemberUpdateView.as_view(),name='member-update'),
    path('team/<int:pk>/delete',MemberDeleteView.as_view(),name='member-delete'),
    path('clubsecy/',views.clubsecy,name = 'clubsecy'),
]
