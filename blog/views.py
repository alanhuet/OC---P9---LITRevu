from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TicketForm, FollowUsersForm, ReviewForm
from .models import Ticket, UserFollows


User = get_user_model()


@login_required
def home(request):
    return render(request, 'blog/home.html')


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    else:
        form = TicketForm()

    return render(request, 'blog/create_ticket.html', {'form': form})


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if ticket.user != request.user:
        return redirect('home')

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm(instance=ticket)

    return render(
        request, 'blog/edit_ticket.html', {'form': form, 'ticket': ticket}
    )


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if ticket.user != request.user:
        return redirect('home')

    if request.method == 'POST':
        ticket.delete()
        return redirect('home')

    return render(request, 'blog/delete_ticket.html', {'ticket': ticket})


@login_required
def subscriptions(request):
    form = FollowUsersForm()

    if request.method == 'POST':
        form = FollowUsersForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user_to_follow = User.objects.get(username=username)

                if user_to_follow == request.user:
                    messages.error(
                        request, 'Vous ne pouvez pas vous suivre vous-même.'
                    )

                elif UserFollows.objects.filter(
                    user=request.user, followed_user=user_to_follow
                ).exists():
                    messages.error(
                        request, f'Vous suivez déjà {user_to_follow.username}'
                    )
                else:
                    UserFollows.objects.create(
                        user=request.user, followed_user=user_to_follow
                    )
                    messages.success(
                        request,
                        f'Vous suivez désormais {user_to_follow.username}'
                    )
                    return redirect('subscriptions')

            except User.DoesNotExist:
                messages.error(
                    request, f"L'utilisateur {username} n'existe pas."
                )

    # Récupération des abonnements et abonnés de l'utilisateur connecté
    following = request.user.following.all()
    followers = request.user.followed_by.all()

    return render(
        request,
        'blog/subscriptions.html',
        {'form': form, 'following': following, 'followers': followers},
    )


@login_required
def unfollow_user(request, follow_id):
    follow = get_object_or_404(UserFollows, id=follow_id, user=request.user)
    if request.method == 'POST':
        follow.delete()
        messages.info(
            request,
            f'Vous ne suivez plus {follow.followed_user.username}.',
        )
    return redirect('subscriptions')


@login_required
def create_ticket_and_review(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()

    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()

            return redirect('home')

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'blog/create_ticket_review.html', context)


@login_required
def create_review_reply(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('home')
    else:
        form = ReviewForm()

    context = {
        'ticket': ticket,
        'form': form,
    }
    return render(request, 'blog/create_review_reply.html', context)
