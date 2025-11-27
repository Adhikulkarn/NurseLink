from django import forms
from django.contrib.auth.models import User
from .models import NurseProfile

class NurseOnboardForm(forms.Form):
    full_name = forms.CharField(max_length=120, required=True)
    phone = forms.CharField(max_length=20, required=True)
    experience = forms.IntegerField(min_value=0, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    certificate = forms.FileField(required=False)

class NurseLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
