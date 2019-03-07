from django.urls import path
from . import views
from users import views as users_views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('register/', users_views.register, name='users-register'),
    path('about/', views.about, name='main-about'),
    path('createchannel/', views.createchannel, name='main-createchannel'),
    path('findchannel/', views.findchannel, name='main-findchannel'),
    path('channelinfo/', views.channelinfo, name='main-channelinfo'),
    path('channelsettings/', views.channelsettings, name='main-channelsettings'),
    path('userprofile/', views.userprofile, name='main-userprofile'),
    path('newmessage', views.newmessage, name='main-newmessage'),
    path('draftpage', views.draftpage, name='main-draftpage'),
]