# admin.py

from django.contrib import admin
from .models import Event, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name',)
    filter_horizontal = ('event_tag',)  # Optional, use if not using Select2
    class Media:
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/css/select2.min.css',)
        }
        js = ('https://code.jquery.com/jquery-3.5.1.min.js', 'https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/js/select2.min.js')
