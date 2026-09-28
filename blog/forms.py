from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        lables = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Image',
        }


class FollowUsersForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={'placeholder': "Saisir le nom d'utilisateur"}
        ),
    )


class ReviewForm(forms.ModelForm):
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
                choices=[(i, f'- {i}') for i in range(6)]
            ),
        }
