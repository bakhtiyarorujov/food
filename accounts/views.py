from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegistrationtForm, LoginForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def change_password(request):
    return render(request, 'change_password.html')

def forget_password(request):
    return render(request, 'forget_password.html')

def login(request):
    next = request.GET.get('next', reverse_lazy('home'))
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request=request, username=form.cleaned_data['username'], password=form.cleaned_data['password']
            )
            if not user:
                messages.add_message(request, messages.ERROR, 'User was not found!')
            else:
                django_login(request, user)
                return redirect(next)
    context = {
        'form': form
    }
    return render(request, 'login.html', context=context)

def register(request):
    form = RegistrationtForm()
    if request.method == 'POST':
        form = RegistrationtForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            return redirect(reverse_lazy('login'))
    context = {
        'form': form
    }
    return render(request, 'register.html', context=context)

def reset_password(request):
    return render(request, 'reset_password.html')

@login_required(login_url='login')
def user_profile(request):
    return render(request, 'user-profile.html')

def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('home'))