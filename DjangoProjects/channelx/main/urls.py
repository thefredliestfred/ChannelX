from django.urls import path, re_path
from . import views
from .views import ChannelListView, ChannelDetailView, ChannelCreateView, ChannelUpdateView, ChannelDeleteView
from users import views as users_views

# Need to later set up path for finding the channel

urlpatterns = [
    path('', ChannelListView.as_view(), name='main-home'),
    path('channel/<int:pk>/', ChannelDetailView.as_view(), name='channel-detail'),
    path('channel/new/', ChannelCreateView.as_view(), name='channel-create'),
    path('channel/<int:pk>/update/', ChannelUpdateView.as_view(), name='channel-update'),
    path('register/', users_views.register, name='users-register'),
    path('channel/<int:pk>/delete/', ChannelDeleteView.as_view(), name='channel-delete'),
    path('about/', views.aboutpage, name='main-about'),
    path('findchannel/', views.findchannelpage, name='main-findchannel'),
    path('channelinfo/', views.channelinfopage, name='main-channelinfo'),
    path('channelsettings/', views.channelsettingspage, name='main-channelsettings'),
    path('userprofile/', users_views.profile, name='profile'),
    path('thankyouregister/', views.thankyouregisterpage, name='main-thankyouregister'),
    path('ticketrecieved/',  views.ticketrecivedpage, name='main-ticketrecieved'),
    path('ticketrequest/',   views.ticketrequestpage, name='main-ticketrequest'),
]
