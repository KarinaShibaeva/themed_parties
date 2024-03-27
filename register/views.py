from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegistrationForm
from .models import User


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Отправка письма с ссылкой для подтверждения регистрации
            send_mail(
                'Подтверждение регистрации',
                'Пожалуйста, перейдите по ссылке для подтверждения регистрации: http://yourwebsite.com/confirm/{0}'.format(
                    user.id),
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return redirect('confirmation_sent')
    else:
        form = UserRegistrationForm()

    return render(request, 'register/register.html', {'form': form})


def confirm_registration(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()

    return render(request, 'register/confirmation.html')
