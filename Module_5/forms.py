from django import forms
from .models import productinfo

class userform(forms.ModelForm):
    class Meta:
        model=productinfo
        fields='__all__'