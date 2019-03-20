from django import forms
from main.models import Channel

class CreateChannelForm(forms.ModelForm):
    channel_name = forms.CharField()
    class Meta:
        model = Channel
        fields = ('channel_name',)