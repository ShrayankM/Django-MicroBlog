from django import forms
from django.forms.widgets import Select
from posts import models
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {
        'class' : 'title form-control'
    }))
    description = forms.CharField(widget = forms.TextInput(attrs = {
        'class' : 'description form-control'
    }))
    category = forms.ModelChoiceField(models.Category.objects.all(),
                                    widget = Select(),
                                    empty_label=('No Category Selected'))
    class Meta:
        model = models.Post
        fields = ('title', 'description', 'category', 'body')

        # widget = {
        #     'category' : forms.Select(choices = models.Category.objects.all().values_list('category', 'category'),
        #                             attrs = {'class' : 'form-control'}),
        # }


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