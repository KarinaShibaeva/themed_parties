from django.contrib import admin

from events.models import Events, Topic, Booking, Comment


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic', 'price', 'date', 'place']
    search_fields = ['name']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['event', 'user', 'number_of_people', 'total_price']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text']
