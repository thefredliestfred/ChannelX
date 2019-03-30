from django import forms
from main.models import Channel

class CreateChannelForm(forms.ModelForm):
    #room_owner = forms.CharField(max_length=40)
    class Meta:
        model = Channel
        fields = ('room_name','expire_date',
        'start_quiet_hour', 'end_quiet_hour')
