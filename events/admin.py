from django.contrib import admin

from events.models import Events, Topic


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic', 'price', 'date', 'place']
    search_fields = ['name']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
