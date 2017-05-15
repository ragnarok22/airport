from django import forms

from model.models import EmergencyReport, SimulationAnalysis


class EmergencyReportCreateForm(forms.ModelForm):
    class Meta:
        model = EmergencyReport
        fields = ['no', 'report', 'datetime', 'place', 'description']
        # widgets = {
        #     'datetime': forms.DateTimeInput(attrs={'class': 'datepicker'})
        # }


class SimulationAnalysisCreateForm(forms.ModelForm):
    class Meta:
        model = SimulationAnalysis
        fields = ['summary', 'evaluation', 'is_necessary_check', 'specify', 'emergency', 'participants']
        # widgets = {
        #     'emergency': forms.ModelChoiceField(
        #         queryset=EmergencyReport.objects.filter(report__contains='s')
        #     )
        # }
