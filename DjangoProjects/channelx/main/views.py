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
    c = Chat.objects.all()
    return render(request, 'main/channelsettings.html', {"title": "Channel Settings", 'channelsettings': 'active', 'chat': c})

def userprofile(request):
    return render(request, 'main/userprofile.html', {"title": "User Profile"})

def newmessage(request):
    return render(request, 'main/newmessage.html', {"title": "New Message"})

def draftpage(request):
    return render(request, 'main/draftpage.html', {"title": "Draft Page"})

#def Post(request):
#    '''
#        This view needs to be edited slightly once it is determined what
#            the table values are
#    '''
#    if request.method == "POST":
#        msg = request.POST.get('msgbox', None)
#        c = Chat(user=request.user, message=msg)
#        if msg != '':
#            c.save()
#        return JsonResponse({'msg': msg})
#    else:
#        return HttpResponse('Request must be POST.')
#
#def Messages(request):
#    c = Chat.objects.all()
#    return render(request, 'main/channelinfo.html', {'chat': c})
#    return render(request, 'main/draftpage.html', {"title": "Draft Page"})
