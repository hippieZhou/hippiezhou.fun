from django.contrib import admin

from .models import Wallpaper
# Register your models here.


@admin.register(Wallpaper)
class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'copyrightonly', 'datetime',)
    search_fields = ('hsh', 'title', 'copyrightonly',)
    list_per_page = 50
    date_hierarchy = 'datetime'
