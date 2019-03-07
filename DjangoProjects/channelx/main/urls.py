from django.urls import path
from . import views
from users import views as users_views

urlpatterns = [
    path('', views.homepage, name='main-home'),
    path('register/', users_views.register, name='users-register'),
    path('about/', views.about, name='main-about'),
    path('createchannel/', views.createchannel, name='main-createchannel'),
    path('findchannel/', views.findchannel, name='main-findchannel'),
    path('channelinfo/', views.channelinfo, name='main-channelinfo'),
    path('channelsettings/', views.channelsettings, name='main-channelsettings'),
    path('userprofile/', views.userprofile, name='main-userprofile'),
    path('newmessage', views.newmessage, name='main-newmessage'),
    path('draftpage', views.draftpage, name='main-draftpage'),
    # Need to add paths for Posting a message and viewing previous messages
    # These two paths can be edited if needed
    path('post/', views.Post, name='post'),
    path('messageLog', views.Messages, name='messageLog'),
    path('about/', views.aboutpage, name='main-about'),
    path('createchannel/', views.createchannelpage, name='main-createchannel'),
    path('findchannel/', views.findchannelpage, name='main-findchannel'),
    path('channelinfo/', views.channelinfopage, name='main-channelinfo'),
    path('channelsettings/', views.channelsettingspage, name='main-channelsettings'),
    path('userprofile/', views.userprofilepage, name='main-userprofile'),
    path('newmessage', views.newmessagepage, name='main-newmessage'),
]
