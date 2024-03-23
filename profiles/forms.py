from django import forms
from .models import Profiles

class ProfileForm(forms.ModelForm):
    """
    Form class for users to create/edit their profile.
    """
    class Meta:
        model = Profiles
        fields = ('title', 'profile_image','content',)
