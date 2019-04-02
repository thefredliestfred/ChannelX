from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Channel
from datetime import date

#@login_required
def homepage(request):
    return render(request, "main/home.html", {"title": "Home"})

class ChannelListView(LoginRequiredMixin, ListView):
    model = Channel
    template_name = "main/home.html"
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

class ChannelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Channel
    template_name = 'main/channelSettings.html'
    fields = ["room_name", "expire_date", "start_quiet_hour", "end_quiet_hour"]

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
    success_url = "/"

    def test_func(self):
        channel = self.get_object()
        if self.request.user == channel.room_owner:
            return True
        return False

def aboutpage(request):
    return render(request, "main/about.html", {"title": "About"})

def findchannelpage(request):
    return render(request, "main/findChannel.html", {"title": "Find Channel"})

def channelinfopage(request):
    return render(request, "main/channelInfo.html", {"title": "Channel Info"})

def channelsettingspage(request):
    return render(request, "main/channelSettings.html", {"title": "Channel Settings"})

def userprofilepage(request):
    return render(request, "main/userProfile.html", {"title": "User Profile"})

def thankyouregisterpage(request):
    return render(request, "main/thankYouReqister.html", {"title": "Thank You"})

def ticketrecivedpage(request):
    return render(request, "main/ticketRecieved.html", {"title": "Ticket Sent"})

def ticketrequestpage(request):
    return render(request, "main/ticketRequest.html", {"title": "Report an Issue"})


#def Post(request):
#    """
#        This view needs to be edited slightly once it is determined what
#            the table values are
#    """
#    if request.method == "POST":
#        msg = request.POST.get("msgbox", None)
#        c = Chat(user=request.user, message=msg)
#        if msg != "":
#            c.save()
#        return JsonResponse({"msg": msg})
#    else:
#        return HttpResponse("Request must be POST.")
#
#def Messages(request):
#    c = Chat.objects.all()
#    return render(request, "main/channelinfo.html", {"chat": c})
#    return render(request, "main/draftpage.html", {"title": "Draft Page"})
