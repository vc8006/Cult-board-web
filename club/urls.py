from django.urls import path
from django.urls import reverse
from . import views
from .views import BlogDetailView,MemberDetailView,AchieveDetailView,PhotoDetailView,EventDetailView,WelcomeDetailView
from .views import BlogCreateView,MemberCreateView,AchieveCreateView,PhotoCreateView,EventCreateView
from .views import BlogUpdateView,MemberUpdateView,AchieveUpdateView,PhotoUpdateView,EventUpdateView,WelcomeUpdateView
from .views import BlogDeleteView,MemberDeleteView,AchieveDeleteView,PhotoDeleteView,EventDeleteView

urlpatterns = [
    path('',views.home,name='club-home'),
    path('events/',views.events,name='club-events'),
    path('achievements/',views.achieve,name='club-achieve'),
    path('gallery/',views.gallery,name='club-gallery'),
    path('blog/',views.blog,name='club-blogs'),
    path('team/',views.team,name='club-team'),
    path('clubsecy/',views.clubsecy,name = 'clubsecy'),

    path('gallery/<int:pk>',PhotoDetailView.as_view(),name='photo-detail'),
    path('gallery/new',PhotoCreateView.as_view(),name='photo-create'),
    path('gallery/<int:pk>/update',PhotoUpdateView.as_view(),name='photo-update'),
    path('gallery/<int:pk>/delete',PhotoDeleteView.as_view(),name='photo-delete'),

    path('blog/<int:pk>',BlogDetailView.as_view(),name='blog-detail'),
    path('blog/new',BlogCreateView.as_view(),name='blog-create'),
    path('blog/<int:pk>/update',BlogUpdateView.as_view(),name='blog-update'),
    path('blog/<int:pk>/delete',BlogDeleteView.as_view(),name='blog-delete'),

    path('event/<int:pk>',EventDetailView.as_view(),name='event-detail'),
    path('event/new',EventCreateView.as_view(),name='event-create'),
    path('event/<int:pk>/update',EventUpdateView.as_view(),name='event-update'),
    path('event/<int:pk>/delete',EventDeleteView.as_view(),name='event-delete'),

    path('achievements/<int:pk>',AchieveDetailView.as_view(),name='achieve-detail'),
    path('achievements/new',AchieveCreateView.as_view(),name='achieve-create'),
    path('achievements/<int:pk>/update',AchieveUpdateView.as_view(),name='achieve-update'),
    path('achievements/<int:pk>/delete',AchieveDeleteView.as_view(),name='achieve-delete'),

    path('team/<int:pk>',MemberDetailView.as_view(),name='member-detail'),
    path('team/new',MemberCreateView.as_view(),name='member-create'),
    path('team/<int:pk>/update',MemberUpdateView.as_view(),name='member-update'),
    path('team/<int:pk>/delete',MemberDeleteView.as_view(),name='member-delete'),

    path('welcome_note/<int:pk>',WelcomeDetailView.as_view(),name='welcomenote-detail'),
    path('welcome_note/<int:pk>/update',WelcomeUpdateView.as_view(),name='welcomenote-update'),

]
