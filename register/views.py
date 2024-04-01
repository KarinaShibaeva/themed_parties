from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import CustomUser, UserProfile


def registration_success(request):
    return render(request, 'register/registration_success.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.send_confirmation_email()
            return redirect('register:registration_success')
    else:
        form = UserRegistrationForm()
    return render(request, 'register/register.html', {'form': form})

def confirm_account(request, confirmation_code):
    user = CustomUser.objects.get(confirmation_code=confirmation_code)
    user.email_verified = True
    user.confirmation_code = ''
    user.save()
    return render(request, 'register/confirm_account.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('auth:profile')  # Перенаправление на личный кабинет
        else:
            # Обработка ошибки, например, неверные учетные данные
            return render(request, 'register/login.html', {'error_message': 'Неправильный логин или пароль'})
    return render(request, 'register/login.html')

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)  # Получаем профиль текущего пользователя
    return render(request, 'register/profile.html', {'user_profile': user_profile})

def logout_user(request):
    logout(request)
    return redirect('home')