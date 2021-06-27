from django import forms
from django.forms import fields
from .models import *


class Home(forms.Form):
    choices = [(1, 'Add a Team Member'),
               (2, 'Add a Gallery Event'),
               (3, 'Add a Major Event'),
               (4, 'Add an Upcoming Event'),
               (5, 'Add a club')]
    choice = forms.ChoiceField(choices=choices)


class TeamMember(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = "__all__"
