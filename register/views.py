from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            send_mail('Confirmation email', 'Please confirm your email by clicking this link: {}'.format(reverse('confirm_email', args=[user.email])), 'from@example.com', [user.email])

            return redirect('registration_success')
    else:
        form = RegistrationForm()

    return render(request, 'register/register.html', {'form': form})

def confirm_email(request, email):
    user = get_user_model().objects.get(email=email)
    user.email_confirmed = True
    user.save()

    return redirect('login')