from django.forms import ModelForm
from django import forms
from App_Login.models import User, Profile

from django.contrib.auth.forms import UserCreationForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user' ,)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    password2 = forms.CharField( label="", widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')






