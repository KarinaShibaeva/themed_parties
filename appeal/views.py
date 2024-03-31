from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from appeal.forms import AppealForm
from events.models import Events


def appeal_view(request):
    context = {"page":"notification_message"}
    return render(request, 'message/notification_message.html', context)


