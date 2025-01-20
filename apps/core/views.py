from django.shortcuts import render, redirect
from .forms import KYCForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = KYCForm(request.FIELS, request.POST)
        if form.is_valid():
            form.save()
            return  redirect('home')
    else:
        form = KYCForm()
    context  = {"form":form}
    return render(request, 'home.html', context)

