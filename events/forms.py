from django import forms

from events.models import Booking


class AppealForm(forms.ModelForm):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Номер телефона')
    number_of_people = forms.IntegerField(label='Количество человек')