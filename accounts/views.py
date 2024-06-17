from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegistrationtForm, LoginForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

User = get_user_model()

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
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
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


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        django_login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')