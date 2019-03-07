from django.shortcuts import render, redirect
from .forms import CreateChannelForm
from .models import Channel

def homepage(request):
    return render(request, 'main/home.html', {"title": "Home"})

def aboutpage(request):
    return render(request, 'main/about.html', {"title": "About"})

def createchannelpage(request):
    return render(request, 'main/createchannel.html', {"title": "Create Channel"})

def findchannelpage(request):
    return render(request, 'main/findchannel.html', {"title": "Find Channel"})

def channelinfopage(request):
    return render(request, 'main/channelinfo.html', {"title": "Channel Info"})

def channelsettingspage(request):
    return render(request, 'main/channelsettings.html', {"title": "Channel Settings"})

def userprofilepage(request):
    return render(request, 'main/userprofile.html', {"title": "User Profile"})

def newmessagepage(request):
    return render(request, 'main/newmessage.html', {"title": "New Message"})

def createchannel(request):
    if request.method == "POST":
        form = CreateChannelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateChannelForm()
    return render(request, "main/createChannel.html", {"form": form})