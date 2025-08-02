from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    summernote_fields = ("description",)
    list_display = ("title", "date", "status", "organizer")
    list_filter = ("status", "date")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Comment)
