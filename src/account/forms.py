from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-4', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-4', 'placeholder': 'Password'}))
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'custom-control-input'}))
