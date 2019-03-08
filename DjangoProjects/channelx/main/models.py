from django.db import models

class Channel(models.Model):
    channel_name = models.CharField(max_length=30)

    def __str__(self):
        return self.channel_name