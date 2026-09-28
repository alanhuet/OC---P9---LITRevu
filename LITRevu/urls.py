"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('home/', blog.views.home, name='home'),
    path('ticket/create/', blog.views.create_ticket, name='create-ticket'),
    path(
        'ticket/<int:ticket_id>/edit/',
        blog.views.edit_ticket,
        name='edit-ticket',
        ),
    path(
        'ticket/<int:ticket_id>/delete/',
        blog.views.delete_ticket,
        name='delete-ticket',
    ),
    path('subscriptions/', blog.views.subscriptions, name='subscriptions'),
    path(
        'subsciptions/<int:follow_id>/unsubscribe/',
        blog.views.unfollow_user,
        name='unfollow',
    ),
    path(
        'review/reate-combined/',
        blog.views.create_ticket_and_review,
        name='create-ticket-review',
    ),
    path(
        'ticket/<int:ticket_id>/reply/',
        blog.views.create_review_reply,
        name='create-review-reply',
    ),
]
