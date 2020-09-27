from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
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
    name = forms.CharField(widget = forms.TextInput(attrs = {
        'class' : 'name form-control',
        'placeholder' : "",
    }))
    email = forms.CharField(widget = forms.EmailInput(attrs = {
        'class' : 'email form-control',
        'placeholder' : "",
    }))
    instagram_link = forms.CharField(widget = forms.URLInput(attrs = {
        'class' : 'instagram form-control',
        'placeholder' : "",
    }))
    profile_pic = forms.ImageField(widget = forms.FileInput(attrs = {
        'class' : 'custom-file-input'
    }))
    class Meta:
        model = models.UserProfile
        fields = ('name', 'email', 'profile_pic', 'instagram_link')