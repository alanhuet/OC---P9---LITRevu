from django import forms

from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    # Formulaire de création et d'édition pour les tickets.
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Image',
        }


class FollowUsersForm(forms.Form):
    # Formulaire permettant de s'abonner à un autre utilisateur via son pseudo.
    username = forms.CharField(
        max_length=150,
        label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={'placeholder': "Saisir le nom d'utilisateur"}
        ),
    )


class ReviewForm(forms.ModelForm):
    # Formulaire de création et d'édition pour les critiques.
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        labels = {
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire',
        }
        widgets = {
            'rating': forms.RadioSelect(
                choices=[(i, f'{i}') for i in range(6)]
            ),
        }
