from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import UserRegistrationFrom
from . models import Account


def UserRegister(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            messages.success(request, f'{first_name} your registration account is created successfully.')
            user.save()   
        else:
            print(form.errors)
            redirect('register')
    else:
        form = UserRegistrationFrom()
    context = {"form":form}
    return render(request, 'account/register.html', context)

