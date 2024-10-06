from django import forms
from .models import URL


class URLShortenerForm(forms.ModelForm):
    class Meta:
        model = URL
        exclude = ("short_url", )
