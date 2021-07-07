from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('clubs/', views.clubs, name='clubs'),
    path('majorEvents/', views.majorEvents, name='majorevents'),
    path('upcomingEvents/', views.upcomingEvents, name='upcomingevents'),
    path('services/', views.services, name='services'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
]
