from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'tags_list', 'created', 'status')
    list_filter = ('status', 'created', 'publish', 'author',)
    search_fields = ('title', 'body',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)

    def tags_list(self, post):
        tag_names = map(lambda x: x.name, post.tags.all())
        return '' if not post.tags else ','.join(tag_names)

    # 只获取当前登录用户对应的文章列表
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(author=request.user)
