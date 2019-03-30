from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

class Channel(models.Model):
    channel_name = models.CharField(max_length=30)
    expire_date = models.DateField(default=date.today, null=True, blank=True)
    start_quiet_hour = models.TimeField(default=datetime.now, blank=True)
    end_quiet_hour = models.TimeField(default=datetime.now, blank=True)
    channel_owner = models.CharField(User, max_length=40)

    def __str__(self):
        return self.channel_name