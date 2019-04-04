# main/routing.py
from django.conf.urls import url
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r'^ws/channel/<str:slug>', consumers.ChatConsumer),
]