from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.crypto import get_random_string

from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2', 'account_type']
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def send_confirmation_email(self):
        user = self.save(commit=False)
        user.confirmation_code = get_random_string(length=20)
        user.save()

        subject = 'Подтверждение аккаунта'
        message = f'Для подтверждения аккаунта перейдите по ссылке: http://yourwebsite.com/confirm/{user.confirmation_code}'
        user.email_user(subject, message)

