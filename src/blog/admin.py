from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'tags', 'body', 'publish', 'status',)
    list_filter = ('status', 'created', 'publish', 'author',)
    search_fields = ('title', 'body',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)
    fieldsets = (
        (None, {
            "fields": ('author',),
        }),
        ('文章', {
            "fields": ('title', 'tags', 'body',),
        }),
        ('设置', {
            "fields": ('publish', 'status',)
        }),
    )

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(author=request.user)
