from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from events.models import Events


class EventsListView(ListView):
    model = Events
    context_object_name = 'events'
    template_name = 'evetns/events_list.html'

def event_id_view(requset, pk):
    pk = get_object_or_404(Events, pk=pk)
    context = {"pk":pk, 'page':'events'}
    return render(requset, "evetns/events_detail.html", context)
