from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Form class for users to request a collaboration
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
