from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING,)
    message = models.TextField()

    def __unicode__(self):
        return self.message
        
class Channel(models.Model):
    channel_name = models.CharField(max_length=30)

    def __str__(self):
        return self.channel_name
