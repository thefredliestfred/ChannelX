from django.urls import path, re_path
from . import views
from .views import ChannelDetailView, ChannelCreateView, ChannelUpdateView, ChannelDeleteView
from users import views as users_views

# Need to later set up path for finding the channel

urlpatterns = [
    path('', views.homepage, name='main-home'),
    path('about/', views.aboutpage, name='main-about'),
    path('channel/new/', ChannelCreateView.as_view(template_name='main/channel_form.html'),
                                                    name='channel-create'),
    path('channel/<slug>/', ChannelDetailView.as_view(), name='channel-detail'),
    path('channel/<slug>/update/', ChannelUpdateView.as_view(), name='channel-update'),
    path('channel/<slug>/delete/', ChannelDeleteView.as_view(), name='channel-delete'),
    path('findchannel/', views.findchannelpage, name='main-findchannel'),
    path('register/', users_views.register, name='users-register'),
    path('profile/', users_views.profile, name='profile'),
    path('channelsettings/', views.channelsettingspage, name='main-channelsettings'),
    path('thankyouregister/', views.thankyouregisterpage, name='main-thankyouregister'),
    path('ticketrecieved/',  views.ticketrecivedpage, name='main-ticketrecieved'),
    path('ticketrequest/',   views.ticketrequestpage, name='main-ticketrequest'),
    path('channel/<str:slug>/', ChannelDetailView.as_view(), name='channel-detail'),
    path('channel/<str:slug>/update/', ChannelUpdateView.as_view(), name='channel-update'),
    path('channel/<str:slug>/delete/', ChannelDeleteView.as_view(), name='channel-delete'),
]
