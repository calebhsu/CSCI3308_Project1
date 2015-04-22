"""forms for taking input from users"""

from django import forms
from matchApp.models import Student, Course, Section
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    """Form for creating new Platypus user"""
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        """Meta defines model and fields for User"""
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
