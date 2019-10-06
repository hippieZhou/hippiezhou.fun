from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Visitor, Soul
# Register your models here.


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip', 'first_time', 'last_time', 'count')
    search_fields = ('ip',)


@admin.register(Soul)
class SoulAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'hits',)
    search_fields = ('title',)
    list_per_page = 20


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('object_repr', 'object_id', 'action_flag', 'user',)
