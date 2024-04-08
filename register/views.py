from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect, get_object_or_404

from events.forms import ProfileForm
from events.models import Booking
from .forms import UserRegistrationForm
from .models import CustomUser, UserProfile


def registration_success(request):
    return render(request, 'register/registration_success.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

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


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('register:profile')
    else:
        form = ProfileForm()

    return render(request, 'register/edit_profile.html', {'form': form})

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)  # Получаем профиль текущего пользователя
    user_booking = Booking.objects.filter(user=request.user)
    return render(request, 'register/profile.html', {'user_profile': user_profile, 'user_booking': user_booking})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('auth:profile')

def logout_user(request):
    logout(request)
    return redirect('siteinfo:main')