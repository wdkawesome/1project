from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import get_user_model

# Create your views here.
def user_login(request):
    """
    Renders the login page.
    """
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    Authenticates the user
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        # Message if invalid username or p/q
        messages.error(request, 'Invalid username or password, please try again.')
        return HttpResponseRedirect(
            reverse('user_auth:login')            
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )
     
def show_user(request):
    """
    Renders the user's dashboard.
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def register_user(request):
    """
    Registers a new user.
    """
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User registered successfully.')
            
            return redirect('home')

        else:
            messages.error(request, 'There was an error with your registration, please see below:')
        
    else:
        form = RegisterUserForm()
        

    return render(request, 'authentication/register_user.html', {'form':form})

def logout_view(request):
    """
    Logs out the user.

    """
    logout(request)
    return redirect('home')