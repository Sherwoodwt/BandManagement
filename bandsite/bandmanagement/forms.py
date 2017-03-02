'''This is where bandmanagement forms are defined'''
from django import forms
from bandmanagement.models import Band, Member

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = [
            'name',
            'picture_url',
        ]

class MemberCreateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'display_name',
            'picture_url',
        ]
