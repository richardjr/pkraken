from django import forms

from .models import UserSettings


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserSettingsForm(forms.ModelForm):
    api_key = forms.CharField(label='API Key', max_length=100)
    elec_mpan = forms.CharField(label='Electricity MPAN', max_length=100)
    elec_serial = forms.CharField(label='Electricity Serial', max_length=100)
    gas_mprn = forms.CharField(label='Gas MPRN', max_length=100)
    gas_serial = forms.CharField(label='Gas Serial', max_length=100)

    class Meta:
        model = UserSettings
        fields = ['api_key', 'elec_mpan', 'elec_serial', 'gas_mprn', 'gas_serial']

