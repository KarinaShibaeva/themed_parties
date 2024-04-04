from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from events.forms import AppealForm
from events.models import Events, Booking


class EventsListView(ListView):
    model = Events
    context_object_name = 'events'
    template_name = 'evetns/events_list.html'

def event_id_view(requset, pk):
    pk = get_object_or_404(Events, pk=pk)
    context = {"pk":pk, 'page':'events'}
    return render(requset, "evetns/events_detail.html", context)


def book_event(request, pk):
    event = Events.objects.get(pk=pk)

    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.event = event
            ticket.total_price = ticket.get_total_price()
            ticket.save()
            return render(request, 'evetns/booking_success.html')
    else:
        form = AppealForm()
    return render(request, 'evetns/booking.html', {'form': form, 'event': event})

def booking_success(request):
    return render(request, 'evetns/booking_success.html')

def booking(request):
    return render(request, 'evetns/booking.html')
