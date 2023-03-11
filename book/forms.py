from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['book', 'full_name', 'email', 'comment_title', 'text']