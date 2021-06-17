from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='club-home'),
    path('events/',views.events,name='club-events'),
    path('gallery/',views.gallery,name='club-gallery'),
    path('blog/',views.blog,name='club-blog'),
    path('achievements/',views.achieve,name='club-achieve'),
    path('team/',views.team,name='club-team'),
]
