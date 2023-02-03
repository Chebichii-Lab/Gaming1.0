from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from gameapp.models import Game, Rate, Profile

# The signup form
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=300, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'profile_picture', 'profile_bio']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ['user','profile']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude = ['user','game','average']