from django.urls import path
from authentication import views

app_name = 'authentication'
urlpatterns = [
    # The home view ('/authentication/')
    path('', views.home, name='home'),
    # Explicit home ('/authentication/home/')
    path('home/', views.home, name='home'),
    # Redirect to get token ('/authentication/gettoken/')
    path('gettoken/', views.gettoken, name='gettoken'),
]
