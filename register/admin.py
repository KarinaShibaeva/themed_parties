from django.contrib import admin

from register.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'account_type', 'email_verified']
