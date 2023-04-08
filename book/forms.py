from django import forms
from django.forms import ModelForm

from .models import AuthorComment, BookComment


class BookCommentForm(ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "نام و نام خانوادگی "}),
    )
    email = forms.CharField(
        max_length=100, widget=forms.EmailInput(attrs={"placeholder": "آدرس ایمیل"})
    )
    body = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={"placeholder": "دیدگاه خود را وارد نمایید"}),
    )

    class Meta:
        model = BookComment
        fields = ["name", "email", "body"]


class AuthorCommentForm(ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "نام و نام خانوادگی "}),
    )
    email = forms.CharField(
        max_length=100, widget=forms.EmailInput(attrs={"placeholder": "آدرس ایمیل"})
    )
    body = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={"placeholder": "دیدگاه خود را وارد نمایید"}),
    )

    class Meta:
        model = AuthorComment
        fields = ["name", "email", "body"]
