from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm
from .models import CustomUser


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
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
        form = RegistrationForm()

    return render(request, 'register/register.html', {'form': form})


def confirm_registration(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.is_active = True
    user.save()

    return render(request, 'confirmation.html')