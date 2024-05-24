from django.shortcuts import render

# Create your views here.
def change_password(request):
    return render(request, 'change_password.html')

def forget_password(request):
    return render(request, 'forget_password.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def reset_password(request):
    return render(request, 'reset_password.html')

def user_profile(request):
    return render(request, 'user-profile.html')