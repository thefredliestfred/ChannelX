from django import forms
from main.models import Channel

class CreateChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ('room_name','expire_date',
        'start_quiet_hour', 'end_quiet_hour')
