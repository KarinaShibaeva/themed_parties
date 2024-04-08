from django import forms

from events.models import Booking, Comment
from register.models import UserProfile


class AppealForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['event', 'total_price', 'user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']