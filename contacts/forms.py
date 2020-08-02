from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message'}))

    class Meta:
        model = Contact
        fields = '__all__'