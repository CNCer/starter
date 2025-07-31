from django import forms
from .models import User, Profile
from django.conf import settings
from concurrency.forms import ConcurrentForm

#class UserUpdateForm(forms.ModelForm):
class UserUpdateForm(ConcurrentForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['user_version', 'username', 'email']

class UserProfileForm(ConcurrentForm):
    language = forms.ChoiceField(choices=settings.LANGUAGES)
    theme = forms.ChoiceField(choices=settings.THEMES)
    class Meta:
        model = Profile
        fields = [ 'profile_version', 'language', 'theme', 'image']