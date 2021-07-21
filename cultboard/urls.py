from django.urls import path
from . import views
from .views import UpcomingEventDetailView,MemberDetailView,MajorEventDetailView,NoteDetailView,GensecDetailView
from .views import UpcomingEventCreateView,MemberCreateView,MajorEventCreateView,GensecCreateView
from .views import UpcomingEventUpdateView,MemberUpdateView,MajorEventUpdateView,NoteUpdateView,GensecUpdateView
from .views import UpcomingEventDeleteView,MemberDeleteView,MajorEventDeleteView,NoteDeleteView,GensecDeleteView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('clubs/', views.clubs, name='clubs'),
    path('majorEvents/', views.majorEvents, name='majorevents'),
    path('upcomingEvents/', views.upcomingEvents, name='upcomingevents'),
    path('services/', views.services, name='services'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('gensec/',views.gensec,name ='gensec'),

    path('major_event/new',MajorEventCreateView.as_view(),name='major_event-create'),
    path('major_event/<int:pk>',MajorEventDetailView.as_view(),name='major_event-detail'),
    path('major_event/<int:pk>/update',MajorEventUpdateView.as_view(),name='major_event-update'),
    path('major_event/<int:pk>/delete',MajorEventDeleteView.as_view(),name='major_event-delete'),

    path('upcoming_event/<int:pk>',UpcomingEventDetailView.as_view(),name='upcoming_event-detail'),
    path('upcoming_event/new',UpcomingEventCreateView.as_view(),name='upcoming_event-create'),
    path('upcoming_event/<int:pk>/update',UpcomingEventUpdateView.as_view(),name='upcoming_event-update'),
    path('upcoming_event/<int:pk>/delete',UpcomingEventDeleteView.as_view(),name='upcoming_event-delete'),

    path('member/<int:pk>',MemberDetailView.as_view(),name='member-detail'),
    path('member/new',MemberCreateView.as_view(),name='member-create'),
    path('member/<int:pk>/update',MemberUpdateView.as_view(),name='member-update'),
    path('member/<int:pk>/delete',MemberDeleteView.as_view(),name='member-delete'),

    path('note/<int:pk>',NoteDetailView.as_view(),name='note-detail'),
    path('note/<int:pk>/update',NoteUpdateView.as_view(),name='note-update'),
    path('note/<int:pk>/delete',NoteDeleteView.as_view(),name='note-delete'),

    path('gensec/<int:pk>',GensecDetailView.as_view(),name='gensec-detail'),
    path('gensec/new',GensecCreateView.as_view(),name='gensec-create'),
    path('gensec/<int:pk>/update',GensecUpdateView.as_view(),name='gensec-update'),
    path('gensec/<int:pk>/delete',GensecDeleteView.as_view(),name='gensec-delete'),

]
