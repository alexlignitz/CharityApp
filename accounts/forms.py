from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.CharField(max_length=64, label="", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=64, label="", widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=28, label="", widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(max_length=28, label="", widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))

    def clean(self):
        data = super().clean()
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise ValidationError("Password does not match")