from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first", "last", "email", "phone"]
        labels = {
            "first": "First Name",
            "last": "Last Name",
        }
