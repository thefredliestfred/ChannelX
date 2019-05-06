from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Channel(models.Model):
    room_name = models.CharField(max_length=30, unique=True)
    start_life = models.DateField(default=date.today, null=True)
    expire_date = models.DateField(default=date.today, null=True)
    start_quiet_hour = models.TimeField(default=datetime.now, blank=True)
    end_quiet_hour = models.TimeField(default=datetime.now, blank=True)
    room_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=30, blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.room_name)
        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.room_name

    def get_absolute_url(self):
        return reverse("channel-detail", kwargs={"slug": self.slug})

class Messages(models.Model):
    room = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True, db_index=True)
    text = models.TextField()

    def to_data(self):
        out = {}
        out['id'] = self.room
        out['from'] = self.user
        out['text'] = self.text
        return out

