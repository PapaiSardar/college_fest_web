from django import forms
from .models import EventDetails

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = ['name', 'roll', 'college_name', 'payment_status', 'events_registered']

    name = forms.CharField(max_length=50)
    roll = forms.IntegerField()
    college_name = forms.CharField(max_length=100)
    payment_status = forms.IntegerField()
    events_registered = forms.CharField(max_length=300)