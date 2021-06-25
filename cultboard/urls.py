from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('clubs/', views.clubs, name='clubs'),
    path('majorEvents/', views.majorEvents, name='clubs'),
    path('upcomingEvents/', views.upcomingEvents, name='clubs'),
    path('services/', views.services, name='clubs'),
    path('aboutUs/', views.aboutUs, name='clubs'),
]