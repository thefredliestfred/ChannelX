from django.urls import path, re_path
from django.conf.urls import include, url
from . import views
from .views import ChannelListView, ChannelDetailView, ChannelCreateView, ChannelUpdateView, ChannelDeleteView
from users import views as users_views

# Need to later set up path for finding the channel

urlpatterns = [
    path('', views.homepage, name='main-home'),
    path('about/', views.aboutpage, name='main-about'),
    path('findchannel/', views.findchannelpage, name='main-findchannel'),
    path('register/', users_views.register, name='users-register'),
    path('profile/', users_views.profile, name='profile'),
    path('channelsettings/', views.channelsettingspage, name='main-channelsettings'),
    path('thankyouregister/', views.thankyouregisterpage, name='main-thankyouregister'),
    path('ticketrecieved/',  views.ticketrecivedpage, name='main-ticketrecieved'),
    path('ticketrequest/',   views.ticketrequestpage, name='main-ticketrequest'),
    path('channel/', ChannelListView.as_view(), name='main-channel-list'),
    path('channel/new/', ChannelCreateView.as_view(), name='channel-create'),
    path('channel/<str:slug>/', ChannelDetailView.as_view(), name='channel-detail'),
    path('channel/<str:slug>/update/', ChannelUpdateView.as_view(), name='channel-update'),
    path('channel/<str:slug>/delete/', ChannelDeleteView.as_view(), name='channel-delete'),
]
