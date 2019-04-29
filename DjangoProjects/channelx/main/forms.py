from django import forms


class Channel(forms.ModelForm):
    class Meta:
        fields = ['room_name', 'start_life', 'expire_date', 'start_quiet_hour',
                  'end_quiet_hour', 'room_owner']


class Ticket(forms.Form):
    tick_info = forms.CharField(widget=forms.Textarea)
