from django.contrib import admin

from .models import Visitor
# Register your models here.


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip', 'first_time', 'last_time',)
    search_fields = ('ip',)
