from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.crypto import get_random_string

from .forms import UserRegistrationForm
from .models import User


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            token = get_random_string(32)
            user.activation_token = token
            user.save()

            send_mail(
                'Activate your account',
                f'Click the link to activate your account: http://{request.get_host()}{reverse("activate, args=[token])}',
                'from@example.com',
                [email],
            )

            return render(request, 'register/confirmation.html')
    else:
        form = UserRegistrationForm()

    return render(request, 'register/register.html', {'form': form})


def activate(request, token):
    user_profile = User.objects.get(activation_token=token)
    user = user_profile.user
    user.is_active = True
    user.save()

    return render(request, 'register/confirmation.html')

