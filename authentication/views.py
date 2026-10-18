from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from . import forms


def signup_page(request):
    """ Gère l'inscription d'un nouvel utilisateur et le connecte
    automatiquement."""
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(
        request, 'authentication/signup.html', context={'form': form}
        )


def logout_user(request):
    # Déconnecte l'utilisateur actif et le redirige vers la page de connexion.
    logout(request)
    return redirect('login')


def login_page(request):
    """ Gère l'authentification et bloque l'accès si l'utilisateur
    est déjà connecté."""
    if request.user.is_authenticated:
        return redirect('home')

    form = forms.LoginForm()
    message = ''

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'identifiants invalides.'
    return render(
        request,
        'authentication/login.html',
        context={'form': form, 'message': message}
        )
