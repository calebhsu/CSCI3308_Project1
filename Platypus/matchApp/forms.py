from django import forms
from matchApp.models import Student, Course, Section
from django.contrib.auth.models import User
from django.db import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'username', 'password')