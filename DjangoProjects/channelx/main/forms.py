from django import forms


class Channel(forms.ModelForm):
    class Meta:
        fields = ['room_name',
                  'start_life',
                  'expire_date',
                  'start_quiet_hour',
                  'end_quiet_hour',
                  'room_owner']

class JoinChannelForm(forms.Form):
    requestedChannel = forms.CharField(label="Channel Name", max_length=30)
    fields = ['room_name', 'start_life', 'expire_date', 'start_quiet_hour',
            'end_quiet_hour', 'room_owner']

class Ticket(forms.Form):
    issue = forms.CharField(max_length=50)
    problem_details = forms.CharField(widget=forms.Textarea)
