from django.contrib.auth.forms import UserCreationForm
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