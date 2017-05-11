from django import forms

from model.models import EmergencyReport


class EmergencyReportCreateForm(forms.ModelForm):
    class Meta:
        model = EmergencyReport
        fields = ['no', 'report', 'datetime', 'place', 'description']
        # widgets = {
        #     'datetime': forms.DateTimeInput(attrs={'class': 'datepicker'})
        # }