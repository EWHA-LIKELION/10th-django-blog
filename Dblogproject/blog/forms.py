from dataclasses import field
from django import forms
from .models import Blog,Comment

class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['username','comment_text']
