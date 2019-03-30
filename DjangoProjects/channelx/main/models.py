from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

class Channel(models.Model):
    room_name = models.CharField(max_length=30)
    expire_date = models.DateField(default=date.today, null=True, blank=True)
    start_quiet_hour = models.TimeField(default=datetime.now, blank=True)
    end_quiet_hour = models.TimeField(default=datetime.now, blank=True)
    room_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.room_name