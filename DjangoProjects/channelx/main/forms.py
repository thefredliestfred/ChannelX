from .models import Channel

def createchannel(request):
    if request.method == "POST":
        form = CreateChannelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateChannelForm()
    return render(request, "main/createChannel.html", {"form": form})

