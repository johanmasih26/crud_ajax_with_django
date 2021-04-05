from django import forms
from django.forms import fields, widgets
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'})
        }







