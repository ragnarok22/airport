from django import forms

from poll.models import NationalPassengerPoll, InternationalPassengerPoll, AirLineRepresentPoll


class NationalPassengerForm(forms.ModelForm):
    class Meta:
        model = NationalPassengerPoll
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'})
        }


class InternationalPassengerForm(forms.ModelForm):
    class Meta:
        model = InternationalPassengerPoll
        fields = '__all__'
        widgets = {
            'date_out': forms.DateInput(attrs={'class': 'datepicker'})
        }


class AirLineRepresentForm(forms.ModelForm):
    class Meta:
        model = AirLineRepresentPoll
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'})
        }
