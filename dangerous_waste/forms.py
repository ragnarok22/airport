from django import forms

from dangerous_waste.models import Waste


class WasteForm(forms.ModelForm):
    class Meta:
        model = Waste
        exclude = ['dangerous_waste']
        widgets = {
            'date_last_measure': forms.DateInput(attrs={'class': 'datepicker'})
        }
