from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Channel, Messages
from datetime import date
from django.utils.safestring import mark_safe
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed
import json


def homepage(request):
    return render(request, "main/home.html", {"title": "Home"})

@login_required
def post(request, slug):
    if request.method == 'POST':
        room = Channel.objects.get(room_name = slug)
        mfrom = request.POST['from']
        text = request.POST['text']

        msg = Message(room=room, user = mfrom, text=text)
        msg.save()
        body = json.dumps(msg.to_data())

        return HttpResponse(body, content_type = 'application/json')
    else:
        room_owner = request.GET.get('user')
        room = Channel.objects.get(slug=slug, room_owner=request.user)
        cmsgs = Messages.objects.filter(
            room=room).order_by('-date')[:50]
        msgs=[]
        for msg in reversed(cmsgs):
            msgs.append(msg.to_data())
        
        return render(request, 'main/channel_detail.html', {'slug' : slug})
    


class ChannelListView(LoginRequiredMixin, ListView):
    model = Channel
    #template_name = "main/channel_list.html"
    context_object_name = "channels"


class ChannelDetailView(LoginRequiredMixin, DetailView):
    model = Channel
    template_name = "main/channel_detail.html"


class ChannelCreateView(LoginRequiredMixin, CreateView):
    model = Channel
    fields = ["room_name", "expire_date", "start_quiet_hour", "end_quiet_hour", "slug"]

    def form_valid(self, form):
        form.instance.room_owner = self.request.user
        form.instance.start_life = date.today()
        #form.instance.slug = room_name
        return super().form_valid(form)

class ChannelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Channel
    template_name = 'main/channelSettings.html'
    fields = ["room_name", "expire_date", "start_quiet_hour", "end_quiet_hour", "slug"]

    def form_valid(self, form):
        form.instance.room_owner = self.request.user
        form.instance.start_life = date.today()
        #form.instance.slug = object.room_name
        return super().form_valid(form)

    def test_func(self):
        channel = self.get_object()
        if self.request.user == channel.room_owner:
            return True
        return False


class ChannelDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Channel
    success_url = "/channel/"

    def test_func(self):
        channel = self.get_object()
        if self.request.user == channel.room_owner:
            return True
        return False


def aboutpage(request):
    return render(request, "main/about.html", {"title": "About"})


@login_required
def findchannelpage(request):
    return render(request, "main/findChannel.html", {"title": "Find Channel"})


@login_required
def channelinfopage(request, room_name):
    return render(request, 'main/channel_detail.html', {'room_name_json': mark_safe(json.dumps(room_name))})


@login_required
def channelsettingspage(request):
    return render(request, "main/channelSettings.html", {"title": "Channel Settings"})


def thankyouregisterpage(request):
    return render(request, "main/thankYouReqister.html", {"title": "Thank You"})


def ticketrecivedpage(request):
    return render(request, "main/ticketRecieved.html", {"title": "Ticket Sent"})


def ticketrequestpage(request):
    return render(request, 'main/ticketRequest.html', {"title": "Report an Issue"})

