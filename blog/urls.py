from django.urls import path

from . import views


urlpatterns = [
    path('ticket/create/', views.create_ticket, name='create-ticket'),
    path(
        'ticket/<int:ticket_id>/edit/',
        views.edit_ticket,
        name='edit-ticket',
        ),
    path(
        'ticket/<int:ticket_id>/delete/',
        views.delete_ticket,
        name='delete-ticket',
    ),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path(
        'subscriptions/<int:follow_id>/unsubscribe/',
        views.unfollow_user,
        name='unfollow',
    ),
    path(
        'review/create-combined/',
        views.create_ticket_and_review,
        name='create-ticket-review',
    ),
    path(
        'ticket/<int:ticket_id>/reply/',
        views.create_review_reply,
        name='create-review-reply',
    ),
    path('posts/', views.user_posts, name='posts'),
    path('feed/', views.feed, name='home'),
    path(
        'review/<int:review_id>/edit/', views.edit_review, name='edit-review'
    ),
    path(
        'review/<int:review_id>/delete/',
        views.delete_review,
        name='delete-review',
    ),
]
