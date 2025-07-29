from django import forms
from .models import User, Profile
from django.conf import settings

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    language = forms.ChoiceField(choices=settings.LANGUAGES)
    theme = forms.ChoiceField(choices=settings.THEMES)
    class Meta:
        model = Profile
        fields = ['language', 'theme', 'image']