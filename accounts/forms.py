from typing import Any, Mapping
from django.contrib.auth.forms import UserCreationForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from accounts.models import Account
from django import forms



class UserRegistrationFrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Confirm Your password", 'class': 'form-control'}))
  
    class Meta:
        model = Account
        fields = ['first_name', 'last_name','phone_number', 'email', 'password']

    
    def clean(self):
        cleaned_data = super(UserRegistrationFrom, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("password don't match!")
        
    def __init__(self, *args, **kwargs):
        super(UserRegistrationFrom, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name '
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name '
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Your phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your Email '
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'