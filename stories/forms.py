from typing import Any
from django import forms
from .models import RecipeComment, Receipe


class CommenttForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = (
            'content',
        )
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Comment',
                'cols': '30',
                'rows': '10'
            })
        }

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Receipe
        fields = (
            'title',
            'content',
            'category',
            'cover',
            'tags'
        )
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description',
                'cols': '30',
                'rows': '10'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control',
            }),             
        }