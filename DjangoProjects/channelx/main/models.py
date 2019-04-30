from django.db import models
from django.utils import timezone
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
    slug = models.SlugField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.room_name)
        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.room_name

    def get_absolute_url(self):
        return reverse("channel-detail", kwargs={"slug": self.slug})


class Ticket(models.Model):
    issue = models.CharField(max_length=50)
    problem_details = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return self.problem_details

    def get_absolute_url(self):
        return reverse('ticketRecieved', kwargs={'pk': self.pk})
