from django import forms

from account.models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'picture', 'born_date', 'gender']
        widgets = {
            'born_date': forms.DateInput(attrs={'class': 'datepicker'})
        }


class ProfileUpdatePasswordForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'is_superuser', 'first_name', 'last_name', 'email', 'is_staff', 'picture',
                  'born_date', 'gender', 'area']
        widgets = {
            'born_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'password': forms.PasswordInput(),
        }
