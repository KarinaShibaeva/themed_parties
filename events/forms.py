from django import forms

from events.models import Booking, Comment


class AppealForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['event', 'total_price', 'user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']