from django import forms

from events.models import Booking


class AppealForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['event', 'total_price', 'user']