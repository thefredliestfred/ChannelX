from django.urls import path
from django.conf.urls import include
from django.urls import path, re_path
from . import views
from users import views as users_views
from . import views
from .views import (
    MemberListView,
    ChannelListView,
    ChannelDetailView,
    ChannelCreateView,
    ChannelUpdateView, 
    ChannelDeleteView,
    TicketCreateView
)

urlpatterns = [
    path('', views.homepage, name='main-home'),
    path('', ChannelListView.as_view()),
    path('about/', views.aboutpage, name='main-about'),
    path('findchannel/', views.join_channel, name='main-findchannel'),
    path('register/', users_views.register, name='users-register'),
    path('profile/', users_views.profile, name='profile'),
    path('channelsettings/', views.channelsettingspage, name='main-channelsettings'),
    path('thankyouregister/', views.thankyouregisterpage, name='main-thankyouregister'),
    path('ticketrecieved/', views.ticketrecivedpage, name='main-ticketrecieved'),
    path('channel/', ChannelListView.as_view(), name='main-channel-list'),
    path('channel/new/', ChannelCreateView.as_view(), name='channel-create'),
    path('channel/<str:slug>/', ChannelDetailView.as_view(), name='channel-detail'),
    path('channel/<str:slug>/update/', ChannelUpdateView.as_view(), name='channel-update'),
    path('channel/<str:slug>/delete/', ChannelDeleteView.as_view(), name='channel-delete'),
    path('ticketrequest/', TicketCreateView.as_view(template_name='main/ticketRequest.html'), name='main-ticketrequest'),

]
