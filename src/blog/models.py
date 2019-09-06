from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from slugify import slugify
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User,
                               verbose_name='作者', on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(verbose_name='标题', max_length=200)
    slug = models.SlugField(verbose_name='格式化', max_length=500, editable=False)
    body = models.TextField(verbose_name='正文')
    created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    published = models.BooleanField(verbose_name='是否发布', default=False)

    class Meta:
        verbose_name = "随笔文章"
        verbose_name_plural = verbose_name
        ordering = ("-updated",)
        index_together = (('id', 'slug'),)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id, self.slug])

    def get_url_path(self):
        return reverse('blog:detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title
