from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from slugify import slugify

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status=True)


class Post(models.Model):
    author = models.ForeignKey(User,
                               verbose_name='作者', on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(verbose_name='标题', max_length=250)
    slug = models.SlugField(
        verbose_name='短标题', max_length=250, editable=False, unique_for_date='publish')
    body = RichTextUploadingField(verbose_name='正文')

    publish = models.DateTimeField(verbose_name='发布时间', default=timezone.now)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    status = models.BooleanField(verbose_name='是否发布', default=False)

    tags = TaggableManager()

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "随笔文章"
        verbose_name_plural = verbose_name
        ordering = ('-publish',)
        index_together = (('id', 'slug'),)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def __str__(self):
        return self.title
