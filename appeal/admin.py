from django.contrib import admin

from appeal.models import Appeal


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['contact', 'events_name']
