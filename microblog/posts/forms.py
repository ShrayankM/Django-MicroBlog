from django import forms
from posts import models
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {
        'class' : 'title form-control'
    }))
    description = forms.CharField(widget = forms.TextInput(attrs = {
        'class' : 'description form-control'
    }))
    class Meta:
        model = models.Post
        fields = ('title', 'description', 'body')


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs = {
        'class' : 'name form-control'
    }))
    body = forms.CharField(widget = forms.TextInput(attrs = {
        'class' : 'body form-control'
    }))
    class Meta:
        model = models.Comment
        fields = ('name', 'body',)