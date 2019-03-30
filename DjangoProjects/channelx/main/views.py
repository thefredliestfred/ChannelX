from django.shortcuts import render, redirect
from django.contrib import messages
from main.forms import CreateChannelForm
from main.models import Channel


def homepage(request):
    channels = Channel.objects.all()
    return render(request, 'main/home.html', {"title": "Home", "channels": channels})

def userprofilepage(request):
    return render(request, 'main/userprofile.html', {"title": "User Profile"})


def aboutpage(request):
    return render(request, 'main/about.html', {"title": "About"})


def findchannelpage(request):
    return render(request, 'main/findChannel.html', {"title": "Find Channel"})


def channelinfopage(request):
    return render(request, 'main/channelInfo.html', {"title": "Channel Info"})


def channelsettingspage(request):
    return render(request, 'main/channelSettings.html', {"title": "Channel Settings"})


def thankyouregisterpage(request):
    return render(request, 'main/thankYouReqister.html', {"title": "Thank You"})


def ticketrecivedpage(request):
    return render(request, 'main/ticketRecieved.html', {"title": "Ticket Sent"})


def ticketrequestpage(request):
    return render(request, 'main/ticketRequest.html', {"title": "Report an Issue"})


def createchannelpage(request):
    if request.method == 'POST':
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        form = CreateChannelForm(request.POST, channel_owner=username)
        if form.is_valid():
            form.save()
            #channelname = form.cleaned_data.get(channel_name)
            #messages.success(request, f'{channelname} was created!')
            return redirect('home')
    else:
        form = CreateChannelForm()
    return render(request, 'main/createChannel.html', {'form': form})
