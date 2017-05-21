from django import forms

from training.models import Training


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        exclude = ['register']
        widgets = {
            'pub_date': forms.DateInput(attrs={'class': 'datepicker'})
        }


class RegisterForm(forms.Form):
    register = forms.BooleanField(label='Registrarse', required=False)
    training = forms.CharField(max_length=10, required=False)
