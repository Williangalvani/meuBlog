from django.forms import ModelForm
from models import FamilySearchDownload

__author__ = 'will'



class SearchForm(ModelForm):
    class Meta:
        model = FamilySearchDownload
        fields = ['filename', 'url']