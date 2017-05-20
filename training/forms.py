from django import forms

from training.models import Training


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        exclude = ['register']
        widgets = {
            'pub_date': forms.DateInput(attrs={'class': 'datepicker'})
        }
