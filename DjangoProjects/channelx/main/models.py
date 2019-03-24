from django.db import models
from datetime import date, datetime

class Channel(models.Model):
    channel_name = models.CharField(max_length=30)
    expire_date = models.DateField(default=date.today, null=True, blank=True)
    start_quiet_hour = models.TimeField(default=datetime.now, blank=True)
    end_quiet_hour = models.TimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.channel_name