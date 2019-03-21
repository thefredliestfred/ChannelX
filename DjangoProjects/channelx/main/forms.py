from django import forms
from main.models import Channel

class CreateChannelForm(forms.ModelForm):
    channel_name = forms.CharField()
    channel_type = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    start_quiet_hour = forms.TimeField()
    end_quiet_hour = forms.TimeField()
    class Meta:
        model = Channel
        fields = ('channel_name','channel_type','start_date','end_date',
        'start_quiet_hour', 'end_quiet_hour')
