from django.db import models

class Channel(models.Model):
    channel_name = models.CharField(max_length=30)
    expire_date = models.DateField()
    start_quiet_hour = models.TimeField()
    end_quiet_hour = models.TimeField()

    def __str__(self):
        return self.channel_name