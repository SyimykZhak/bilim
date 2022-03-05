from django import forms
from .models import Contacts

class UserForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('name', 'email', 'description','telephone','addres')

    