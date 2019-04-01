# main/routing.py
from django.conf.urls import url
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/channel/<int:pk>(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]