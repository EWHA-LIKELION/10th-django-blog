from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
  class Mata:
    model = Blog
    fields = ['title', 'body', 'photo']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['username', 'comment_text']