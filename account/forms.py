from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Give a creative title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Express yourself..'}),
        }