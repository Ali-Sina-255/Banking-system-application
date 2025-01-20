from django.shortcuts import render, redirect
from .forms import KYCForm
from ..accounts.models import Account, KYCModel


# Create your views here.
def home(request):
    user = request.user
    account = Account.objects.get(user=user)
    try:
        kyc = KYCModel.objects.get(user=user)
    except:
        kyc = None

    if request.method == 'POST':
        form = KYCForm(request.FIELS, request.POST,instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user =user
            new_form.account = account




            return  redirect('home')
    else:
        form = KYCForm()
    context  = {"form":form}
    return render(request, 'home.html', context)

