from django.urls import path
from . import views
from users import views as users_views

urlpatterns = [
    path('', views.homepage, name='main-home'),
    path('register/', users_views.register, name='users-register'),
    path('about/', views.aboutpage, name='main-about'),
    path('createchannel/', views.createchannelpage, name='main-createchannel'),
    path('findchannel/', views.findchannelpage, name='main-findchannel'),
    path('channelinfo/', views.channelinfopage, name='main-channelinfo'),
    path('channelsettings/', views.channelsettingspage, name='main-channelsettings'),
    path('userprofile/', views.userprofilepage, name='main-userprofile'),
    path('login/', views.loginpage, name='main-login'),
    path('thankyouregister/', views.thankyouregisterpage, name='main-thankyouregister'),
    path('ticketrecieved/',  views.ticketrecivedpage, name='main-ticketrecieved'),
    path('ticketrequest/',   views.ticketrequestpage, name='main-ticketrequest'),
]
