from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts import models
from django import forms

class UserForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {
        'class' : 'username form-control',
        'placeholder' : "",
    }))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'password1 form-control',
        'placeholder' : "",
    }))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'password2 form-control',
        'placeholder' : "",
    }))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ('firstname', 'lastname','email', 'profile_pic', 'instagram_link')