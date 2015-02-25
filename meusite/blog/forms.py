__author__ = 'will'

from pagedown.widgets import AdminPagedownWidget
from django import forms
from models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget(show_preview=True))

    class Meta:
        model = Post