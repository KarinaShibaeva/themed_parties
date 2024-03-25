from django.urls import path

from events.views import EventsListView, event_id_view

app_name = 'events'

urlpatterns = [
    path('', EventsListView.as_view(), name='events'),
    path('<int:pk>', event_id_view, name='event_detail')
]