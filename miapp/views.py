from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.views.generic.edit import FormView
from .forms import registerForm
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Usuario Incorrecto')
    return render(request, 'users/indexLogin.html')

def registerUser(request):
    register_Form = registerForm()

    if request.method == 'POST':
       register_Form = registerForm(request.POST) 
       if register_Form.is_valid():
           register_Form.save()
           messages.success(request, 'Registrado Correctamente')
           return redirect('home')

    return render(request, 'users/registerUser.html', {
        'register_Form': register_Form
    })

def logoutUser(request):
    logout(request)
    return redirect('indexLogin')

def home(request):
    return render(request, 'users/home.html')


    