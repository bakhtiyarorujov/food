from typing import Any
from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):
    # surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Your Surname'
    # }))
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'cols': '30',
                'rows': '7'
            })
        }
    
    # def clean_email(self):
    #     value = self.cleaned_data['email']
    #     if not value.endswith('gmail.com'):
    #         raise forms.ValidationError('Email must be gmail form!')
    #     return value

    def clean_name(self):
        value = self.cleaned_data['name']
        return value.lower()

    # def clean(self) -> dict[str, Any]:
    #     value = self.cleaned_data['email']
    #     if not value.endswith('gmail.com'):
    #         raise forms.ValidationError('Email must be gmail form!')
    #     return super().clean()