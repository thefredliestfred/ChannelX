from django.contrib import admin
from .models import Channel, ChannelMembers

admin.site.register(Channel)
admin.site.register(ChannelMembers)