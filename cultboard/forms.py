from django import forms


class TeamMember(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    pic = forms.ImageField(label='Photo of member', required=False)
    position = forms.CharField(label='Position of Member')
    phone_number = forms.CharField(
        label='Phone Number of Member', max_length=10)
    email = forms.CharField(label='E-Mail of Member')
