from django import forms
from App_Complain.models import UserComplain

class ComplainForm(forms.ModelForm):
    class Meta:
        model = UserComplain
        exclude = ('user',) 