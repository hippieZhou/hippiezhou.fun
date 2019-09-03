from django.contrib import admin

from .models import Wallpaper
# Register your models here.


@admin.register(Wallpaper)
class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('hsh', 'title', 'copyrightonly', 'datetime',)
    search_fields = ('hsh', 'title', 'copyrightonly',)
