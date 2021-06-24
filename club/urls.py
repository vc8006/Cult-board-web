from django.urls import path
from . import views
urlpatterns =[
path('',views.index,name='index'),
path('culbEvents/',views.ClubEventsView.as_view(),name='clubEvents'),
path('clubEvent/<int:pk>',views.EventDetailView.as_view(),name='event-detail'),
]
