from django import forms

from bulletin.models import Bulletin


class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = '__all__'
        widgets = {
            'pub_date': forms.DateInput(attrs={'class': 'datepicker'})
        }
