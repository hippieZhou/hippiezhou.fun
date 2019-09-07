from django.contrib import admin
from .models import ArticlePost
# Register your models here.


@admin.register(ArticlePost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'updated', 'published',)
    search_fields = ('title', 'body',)
