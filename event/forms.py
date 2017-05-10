from django import forms

from event.models import Event


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'})
        }
