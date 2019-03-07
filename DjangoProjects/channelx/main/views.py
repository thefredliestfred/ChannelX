from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html', {"title": "Home"})

def about(request):
    return render(request, 'main/about.html', {"title": "About"})

def createchannel(request):
    return render(request, 'main/createchannel.html', {"title": "Create Channel"})

def findchannel(request):
    return render(request, 'main/findchannel.html', {"title": "Find Channel"})

def channelinfo(request):
    return render(request, 'main/channelinfo.html', {"title": "Channel Info"})

def channelsettings(request):
    return render(request, 'main/channelsettings.html', {"title": "Channel Settings"})

def userprofile(request):
    return render(request, 'main/userprofile.html', {"title": "User Profile"})

def newmessage(request):
    return render(request, 'main/newmessage.html', {"title": "New Message"})

def draftpage(request):
    return render(request, 'main/draftpage.html', {"title": "Draft Page"})