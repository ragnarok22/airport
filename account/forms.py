from django import forms

from account.models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'picture', 'born_date', 'sex']


class ProfileUpdatePasswordForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['password']
        widgets = {
            'password': forms.PasswordInput(),
        }
