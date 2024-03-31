from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import CustomUser


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.send_confirmation_email()
            return redirect('registration_success')
    else:
        form = UserRegistrationForm()
    return render(request, 'register/register.html', {'form': form})

def confirm_account(request, confirmation_code):
    user = CustomUser.objects.get(confirmation_code=confirmation_code)
    user.email_verified = True
    user.confirmation_code = ''
    user.save()
    return render(request, 'register/confirm_account.html')
