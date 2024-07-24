from django import forms
from .models import User, Profile


class LoginForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
