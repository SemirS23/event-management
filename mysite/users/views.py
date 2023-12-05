from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            auth = authenticate(request, username=username, password=password)
            if auth is not None:
                login(request, user)
                return redirect('eticket:home')
            else:
                messages.error(request, 'The Password is Incorrect')
        except Exception as e:
            messages.error(request, "The username does Not Exist")

    context = {}
    return render(request, "users/login.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Account.objects.create(
                user = user,
                balance = 0
            )
            return redirect('users:loginPage')
        else:
            messages.error(request, 'Could Not Register account')

    context = {'form':form}
    return render(request, "users/registration.html", context)

def logoutPage(request):
    logout(request)
    return redirect('users:loginPage') 