'''This is where bandmanagement forms are defined'''
from django import forms
from bandmanagement.models import Band

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = [
            'name',
            'picture_url',
        ]
