from django.utils.safestring import mark_safe

__author__ = 'will'

from django import forms
from models import Post

class ExpandedTextArea(forms.Textarea):
    def __init__(self, attrs=None):
        super(ExpandedTextArea, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        return mark_safe("""<div class="wmd-wrapper">
    <div class="wmd-panel input">
        <div class="wmd_button_bar"></div>
        {0}
    </div>
        <div class="wmd-panel wmd-preview"></div>

</div>""".format(super(ExpandedTextArea, self).render(name, value, attrs=None)))


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = []
        widgets = {
            'body': ExpandedTextArea(attrs={'class':'codemirror',})}