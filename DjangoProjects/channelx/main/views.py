from datetime import date, datetime
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Channel, ChannelMembers, Ticket
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from main.forms import JoinChannelForm

def homepage(request):
    return render(request, "main/home.html", {"title": "Home"})

@login_required
def join_channel(request):
    if request.method == 'POST':
        form = JoinChannelForm(request.POST)
        if form.is_valid():
            try:
                cname = form.cleaned_data.get("requestedChannel")
                cid = Channel.objects.get(room_name=cname).id
                new_member = ChannelMembers()
                new_member.channel_id = cid
                new_member.member_id = request.user.id
                new_member.save()
                messages.success(request, f'You have joined {cname}')
                return redirect("main-findchannel")
            except ChannelMembers.DoesNotExist:
                messages.success(request, f'Channel does not exist')
                return redirect("main-findchannel")
    else:
        form = JoinChannelForm()
    return render(request, 'main/findChannel.html', {'form': form})

class BaseLayout(ListView):
    model = Channel
    context_object_name = "channels"
    template_name = "main/base.html"
    
class ChannelListView(ListView):
    model = Channel
    context_object_name = "channels"

class MemberListView(LoginRequiredMixin, ListView):
    model = ChannelMembers
    template_name = "main/channel_detail.html"

class ChannelDetailView(LoginRequiredMixin, DetailView):
    model = Channel
    template_name = "main/channel_detail.html"

class ChannelCreateView(LoginRequiredMixin, CreateView):
    model = Channel
    fields = ["room_name", "expire_date", "start_quiet_hour", "end_quiet_hour", "slug"]

    def form_valid(self, form):
        form.instance.room_owner = self.request.user
        form.instance.start_life = date.today()
        return super().form_valid(form)


class ChannelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Channel
    template_name = 'main/channelSettings.html'
    fields = ["room_name", "expire_date", "start_quiet_hour", "end_quiet_hour", "slug"]

    def form_valid(self, form):
        form.instance.room_owner = self.request.user
        form.instance.start_life = date.today()
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

class TicketCreateView(CreateView):
    model = Ticket
    template_name = 'main/tickeRequest.html'
    fields = ['issue', 'problem_details']
    now = datetime.now()

    def form_valid(self, form):
        form.instance.author = self.request.user
        send_mail(f'Ticket created by {form.instance.author} {self.now}', f'{self.fields}', 'WTAMU ChannelX Tickets', [f'wtchanx2019@gmail.com',])
        return redirect('main-ticketrecieved')

def aboutpage(request):
    return render(request, "main/about.html", {"title": "About"})

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
    