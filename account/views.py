from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from django.http import HttpResponse
from account.form import RegistrationForm, AccountAuthenticationForm


#def register(request):
#
#    form = RegistrationForm()
#    context = {'form': form}
#
#    if request.method == 'POST':
#        form = RegistrationForm(request.POST)
#
#        if form.is_valid():
#            form.save()
#            email = form.cleaned_data['email']
#            password = form.cleaned_data['password1']
#            user = authenticate(email=email, password=password)
#            login(request, user)
#            return render(request, 'home/main.html', context)
#        else:
#            return HttpResponse('Data is not clean', form.errors)
#    else:
#        return render(request, 'registration/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def login_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
            return redirect('main')
        else:
            raise ValueError('Email or Password is invalid')
    else:
        form = AccountAuthenticationForm()
    context = {'form': form}
    return render(request, 'account/home.html', context)
