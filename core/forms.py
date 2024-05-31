from accounts.models import  KYCModel
from django import forms


class KYCForm(forms.ModelForm):
    images = forms.FileField(widget=forms.FileField(attrs={'class':'btn btn-info'}))
    identity_image = forms.FileField(widget=forms.FileField(attrs={'class':'btn btn-info'}))

    class Meta:
        model = KYCModel
        excludes =['id','user']
        widgets = {
            'full_name':forms.IextInput(attrs={"placeholder":"Full Name"})
        }