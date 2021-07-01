from django import forms
from django.forms import fields
from .models import *

choices = [(1, 'Add a Team Member'),
           (2, 'Add a Gallery Event'),
           (3, 'Add a Major Event'),
           (4, 'Add an Upcoming Event'),
           (5, 'Add a club')]


class teamMember(forms.ModelForm):
    choice = forms.ChoiceField(choices=choices, widget=forms.Select(
        attrs={'onchange': 'loadDoc();'}))

    class Meta:
        model = TeamMember
        fields = "__all__"


class majorEvent(forms.ModelForm):
    choice = forms.ChoiceField(choices=choices, widget=forms.Select(
        attrs={'onchange': 'loadDoc(this.value);'}))

    class Meta:
        model = MajorEvent
        fields = "__all__"
