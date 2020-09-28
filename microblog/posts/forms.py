from django import forms
from posts import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'body')


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('name', 'body',)