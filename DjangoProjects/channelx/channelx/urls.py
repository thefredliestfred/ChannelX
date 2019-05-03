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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from users import views as user_views
from main import urls as main_urls

# Need to later set up path for finding the channel

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('profile/', user_views.profile, name='profile'),
    path('pword_reset/', auth_views.PasswordResetView.as_view(
     template_name='users/pword_reset.html'),
         name='pword_reset'),
    path('pword_reset/done/', auth_views.PasswordResetDoneView.as_view(
             template_name='users/pword_reset_done.html'), name='pword_reset_done'),
    path('pword_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
             template_name='users/pword_reset_confirm.html'), name='pword_reset_confirm'),
    path('pword_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
             template_name='users/pword_reset_complete.html'), name='pword_reset_complete'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
