from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegistrationForm

def register_user(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data['password1']
        user.set_password(password)
        user.save()

        # Отправка приветственного письма
        subject = 'Добро пожаловать!'
        message = f'Привет, {user.username}! Спасибо за регистрацию на нашем сайте.'
        sender = settings.EMAIL_HOST_USER
        recipient = [user.email]

        send_mail(subject, message, sender, recipient, fail_silently=False)

        return redirect('registration_success')

    return render(request, 'register/register.html', {'form': form})
