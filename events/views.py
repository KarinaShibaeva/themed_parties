from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from events.models import Events, Booking


class EventsListView(ListView):
    model = Events
    context_object_name = 'events'
    template_name = 'evetns/events_list.html'

def event_id_view(requset, pk):
    pk = get_object_or_404(Events, pk=pk)
    context = {"pk":pk, 'page':'events'}
    return render(requset, "evetns/events_detail.html", context)


def book_event(request, event_id):
    if request.method == 'POST':
        event = Events.objects.get(id=event_id)
        booking = Booking(event=event, user=request.user)
        booking.total_price = booking.number_of_people * booking.price
        booking.save()
        return redirect('booking_success')
    else:
        return redirect('event_id_view', event_id=event_id)

def booking_success(request):
    return render(request, 'evetns/booking_success.html')
