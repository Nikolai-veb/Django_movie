from django.contrib import admin

from .models import Contacts


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "date")
