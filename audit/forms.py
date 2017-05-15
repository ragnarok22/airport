from django import forms

from audit.models import Audit


class AuditForm(forms.ModelForm):
    class Meta:
        model = Audit
        exclude = ['general_program']
