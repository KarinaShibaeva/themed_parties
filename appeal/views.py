from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from appeal.forms import AppealForm
from events.models import Events


def appeal_view(request):
    context = {"page":"notification_message"}
    return render(request, 'message/notification_message.html', context)

def submit_appeal(request, event_id):
    event = Events.objects.get(id=event_id)
    if request.method == 'POST':
        form = AppealForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.event = event
            reservation.save()
            return render(request, 'message/notification_message.html')  # Перенаправление на страницу благодарности после успешной отправки заявки
    else:
        form = AppealForm()

    return render(request, 'appeal/appeal.html', {'event': event, 'form': form})
