from django import forms

from model.models import EmergencyReport, SimulationAnalysis, Communication


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


class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = ['airport_name', 'year', 'reception_way', 'type_communication', 'contact_data', 'info_content',
                  'adopted_decision', 'distribution_date', 'emission_path']
        widgets = {
            'distribution_date': forms.DateInput(attrs={'class': 'datepicker'})
        }