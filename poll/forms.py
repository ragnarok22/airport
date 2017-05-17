from django import forms

from poll.models import NationalPassengerPoll


class NationalPassengerForm(forms.ModelForm):
    class Meta:
        model = NationalPassengerPoll
        fields = '__all__'
