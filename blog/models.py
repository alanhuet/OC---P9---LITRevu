from django.db import models
from django.conf import settings
from authentication.models import User


class Ticket(models.Model):
    title = models.fields.CharField(max_length=128)
    description = models.fields.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        User,
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    ticket = models.ForeignKey(Ticket, to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(max_length=1024, validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    user = models.ForeignKey(
        User,
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    headline = models.fields.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    class Meta(models.Model.Meta):
        unique_together = ('user', 'followed_user', )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following'
        )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by'
        )
