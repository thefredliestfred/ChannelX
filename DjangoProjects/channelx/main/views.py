from django.shortcuts import render, redirect
from main.forms import CreateChannelForm

def homepage(request):
    return render(request, 'main/home.html', {"title": "Home"})

def aboutpage(request):
    return render(request, 'main/about.html', {"title": "About"})

def findchannelpage(request):
    return render(request, 'main/findChannel.html', {"title": "Find Channel"})

def channelinfopage(request):
    return render(request, 'main/channelInfo.html', {"title": "Channel Info"})

def channelsettingspage(request):
    return render(request, 'main/channelSettings.html', {"title": "Channel Settings"})

def userprofilepage(request):
    return render(request, 'main/userProfile.html', {"title": "User Profile"})

def newmessagepage(request):
    return render(request, 'main/newMessage.html', {"title": "New Message"})

def createchannelpage(request):
    if request.method == 'POST':
        form = CreateChannelForm(request.POST)
        if form.is_valid():
            form.save()
            channelname = form.cleaned_data.get('channel_name')
            #messages.success(request, f'{channelname} was created!')
            return redirect('/')
    else:
        form = CreateChannelForm()
    return render(request, 'main/createChannel.html', {'form': form})
    
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
