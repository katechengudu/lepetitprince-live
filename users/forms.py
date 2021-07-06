from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisgerForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta(UserCreationForm):
        model = User
        fields = ('username','password1','password2')
