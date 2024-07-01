from django import forms
from .models import ContactForm

class ContactForms(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 5}),
        }