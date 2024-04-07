from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from events.forms import AppealForm, CommentForm
from events.models import Events, Booking


class EventsListView(ListView):
    model = Events
    context_object_name = 'events'
    template_name = 'evetns/events_list.html'

def event_id_view(request, pk):
    pk = get_object_or_404(Events, pk=pk)
    comments = pk.comment_set.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pk = pk  # изменено с pk на event
            new_comment.save()
    else:
        form = CommentForm()

    return render(request, 'evetns/events_detail.html', {'pk': pk, 'comments': comments, 'form': form})


def book_event(request, pk):
    event = Events.objects.get(pk=pk)
    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            user = request.user
            number_of_people = form.cleaned_data['number_of_people']
            total_price = event.price * number_of_people
            booking = Booking(event=event, number_of_people=number_of_people, total_price=total_price, user=user)
            booking.save()
            return redirect('events:success', pk=pk)
    else:
        form = AppealForm()

    return render(request, 'evetns/booking.html', {'event': event, 'form': form})

def booking_success(request, pk):
    return render(request, 'evetns/booking_success.html', {'pk':pk})

def booking(request):
    return render(request, 'evetns/booking.html')
