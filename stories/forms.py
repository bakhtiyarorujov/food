from typing import Any
from django import forms
from .models import RecipeComment


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