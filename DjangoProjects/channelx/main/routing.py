# main/routing.py
from django.conf.urls import url
from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path(r'^ws/channel/<slug>', consumers.ChatConsumer),
]