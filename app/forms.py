from app.models import *
from django import forms

class UserForm(forms.ModelForm):    
    class Meta:
        model = UserModel
        fields = ['email']