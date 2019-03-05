"""channelx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from main import urls as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', include('main.urls')),
    path('about/', include('main.urls')),
    path('createchannel/', include('main.urls')),
    path('findchannel/', include('main.urls')),
    path('channelinfo/', include('main.urls')),
    path('channelsettings/', include('main.urls')),
    path('userprofile/', include('main.urls')),
    path('newmessage/', include('main.urls')),
    path('draftpage/', include('main.urls')),
]