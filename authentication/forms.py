from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    # Formulaire d'inscription
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)


class LoginForm(forms.Form):
    # Formulaire de validation pour la connexion utilisateur.
    username = forms.CharField(max_length=63, label="nom d'utilisateur")
    password = forms.CharField(
        max_length=63, widget=forms.PasswordInput, label="mot de passe"
        )
