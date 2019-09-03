from django.db import models

# Create your models here.


class Wallpaper(models.Model):
    hsh = models.CharField(verbose_name='唯一标识', max_length=48)

    title = models.CharField(verbose_name='标题', max_length=100)
    caption = models.CharField(verbose_name='主题', max_length=100)
    desc = models.TextField(verbose_name='内容')

    copyright = models.CharField(verbose_name='完整版权信息', max_length=200)
    copyrightonly = models.CharField(verbose_name='基本版权信息', max_length=100)
    copyrightlink = models.URLField(verbose_name='版权地址')

    datetime = models.DateTimeField(verbose_name='日期')

    quiz = models.URLField(verbose_name='详情地址')
    url = models.URLField(verbose_name='图片地址')
    urlbase = models.URLField(verbose_name='基地址')

    class Meta:
        verbose_name = "必应壁纸"
        verbose_name_plural = verbose_name
        ordering = ('-datetime',)

    def __str__(self):
        return self.title
