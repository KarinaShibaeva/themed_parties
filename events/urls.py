from django.urls import path

from events.views import EventsListView, event_id_view, book_event, booking

app_name = 'events'

urlpatterns = [
    path('', EventsListView.as_view(), name='events'),
    path('<int:pk>/', event_id_view, name='event_detail'),
    path('<int:pk>/booking', book_event, name='book_event'),
    path('<int:pk>/booking/success', book_event, name='success')
]