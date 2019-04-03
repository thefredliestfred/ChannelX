from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# from main.forms import CreateChannelForm
from main.models import Channel
from datetime import date
from django.utils.safestring import mark_safe

import json

@login_required
def homepage(request):
    return render(request, "main/home.html", {"title": "Home"})

class ChannelListView(ListView):
    model = Channel
    template_name = "main/home.html" # <app>/<model>_<viewtype>.html
    context_object_name = "channels"

class ChannelDetailView(LoginRequiredMixin, DetailView):
    model = Channel

class ChannelCreateView(LoginRequiredMixin, CreateView):
    model = Channel
    fields = ["room_name", "expire_date", "start_quiet_hour", "end_quiet_hour"]

    def form_valid(self, form):
        form.instance.room_owner = self.request.user
        form.instance.start_life = date.today()
        return super().form_valid(form)

class ChannelUpdateView(LoginRequiredMixin, UpdateView):
    model = Channel
    fields = ["room_name", "expire_date", "start_quiet_hour", "end_quiet_hour"]

    def form_valid(self, form):
        form.instance.room_owner = self.request.user
        form.instance.start_life = date.today()
        return super().form_valid(form)


def userprofilepage(request):
    return render(request, 'users/profile.html', {"title": "User Profile"})


def aboutpage(request):
    return render(request, "main/about.html", {"title": "About"})


def findchannelpage(request):
    return render(request, "main/findChannel.html", {"title": "Find Channel"})


def channelsettingspage(request):
    return render(request, "main/channelSettings.html", {"title": "Channel Settings"})


def thankyouregisterpage(request):
    return render(request, "main/thankYouReqister.html", {"title": "Thank You"})


def ticketrecivedpage(request):
    return render(request, "main/ticketRecieved.html", {"title": "Ticket Sent"})


def ticketrequestpage(request):
    return render(request, 'main/ticketRequest.html', {"title": "Report an Issue"})


#def createchannelpage(request):
#    if request.method == 'POST':
#        username = None
#        if request.user.is_authenticated():
#            username = request.user.username
#        form = CreateChannelForm(request.POST, channel_owner=username)
#        if form.is_valid():
#            form.save()
#            #channelname = form.cleaned_data.get(channel_name)
#            #messages.success(request, f'{channelname} was created!')
#            return redirect(' ')
#    else:
#        form = CreateChannelForm()
#    return render(request, 'main/createChannel.html', {'form': form})
