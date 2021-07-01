from django.urls import path
from django.urls import reverse 
from . import views
from .views import BlogDetailView,MemberDetailView,AchieveDetailView,PhotoDetailView,EventDetailView,WelcomeDetailView
from .views import BlogCreateView,MemberCreateView,AchieveCreateView,PhotoCreateView,EventCreateView
from .views import BlogUpdateView,MemberUpdateView,AchieveUpdateView,PhotoUpdateView,EventUpdateView,WelcomeUpdateView
from .views import BlogDeleteView,MemberDeleteView,AchieveDeleteView,PhotoDeleteView,EventDeleteView

urlpatterns = [
    path('',views.main_page,name='home'),
    path('Club/',views.home,name='club-home'),
    path('Club/events/',views.events,name='club-events'),
    path('Club/achievements/',views.achieve,name='club-achieve'),
    path('Club/gallery/',views.gallery,name='club-gallery'),
    path('Club/blog/',views.blog,name='club-blogs'),
    path('Club/team/',views.team,name='club-team'),
    path('Club/clubsecy/',views.clubsecy,name = 'clubsecy'),

    path('Club/gallery/<int:pk>',PhotoDetailView.as_view(),name='photo-detail'),
    path('Club/gallery/new',PhotoCreateView.as_view(),name='photo-create'),
    path('Club/gallery/<int:pk>/update',PhotoUpdateView.as_view(),name='photo-update'),
    path('Club/gallery/<int:pk>/delete',PhotoDeleteView.as_view(),name='photo-delete'),
    
    path('Club/blog/<int:pk>',BlogDetailView.as_view(),name='blog-detail'),
    path('Club/blog/new',BlogCreateView.as_view(),name='blog-create'),
    path('Club/blog/<int:pk>/update',BlogUpdateView.as_view(),name='blog-update'),
    path('Club/blog/<int:pk>/delete',BlogDeleteView.as_view(),name='blog-delete'),
    
    path('Club/event/<int:pk>',EventDetailView.as_view(),name='event-detail'),
    path('Club/event/new',EventCreateView.as_view(),name='event-create'),
    path('Club/event/<int:pk>/update',EventUpdateView.as_view(),name='event-update'),
    path('Club/event/<int:pk>/delete',EventDeleteView.as_view(),name='event-delete'),

    path('Club/achievements/<int:pk>',AchieveDetailView.as_view(),name='achieve-detail'),
    path('Club/achievements/new',AchieveCreateView.as_view(),name='achieve-create'),
    path('Club/achievements/<int:pk>/update',AchieveUpdateView.as_view(),name='achieve-update'),
    path('Club/achievements/<int:pk>/delete',AchieveDeleteView.as_view(),name='achieve-delete'),
    
    path('Club/team/<int:pk>',MemberDetailView.as_view(),name='member-detail'),
    path('Club/team/new',MemberCreateView.as_view(),name='member-create'),
    path('Club/team/<int:pk>/update',MemberUpdateView.as_view(),name='member-update'),
    path('Club/team/<int:pk>/delete',MemberDeleteView.as_view(),name='member-delete'),

    path('Club/welcome_note/<int:pk>',WelcomeDetailView.as_view(),name='welcomenote-detail'),
    path('Club/welcome_note/<int:pk>/update',WelcomeUpdateView.as_view(),name='welcomenote-update'),

]
