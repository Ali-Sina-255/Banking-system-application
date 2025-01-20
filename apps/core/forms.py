from apps.accounts.models import  KYCModel
from django import forms
from django.forms import  ImageField,FileInput

class DateInput(forms.DateInput):
    input_type = 'date'


class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    images = ImageField(widget=FileInput)

    class Meta:
        model = KYCModel
        fields= ['full_name',"images","marrital_status","gender","identity_id","identity_image","date_of_birth","signature",'country',"city","state","mobile"]
        widgets = {
            'full_name':forms.TextInput(attrs={"placeholder":"Full Name","class":""}),
            'mobile':forms.TextInput(attrs={"placeholder":"Mobile Number . ","class":""}),
            'country':forms.TextInput(attrs={"placeholder":"Country Name . ","class":""}),
            'state':forms.TextInput(attrs={"placeholder":"State Name . ","class":""}),
            'city':forms.TextInput(attrs={"placeholder":"City Name . ","class":""}),
        }