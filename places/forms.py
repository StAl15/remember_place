from django import forms
from .models import Places


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ("place", "description")
