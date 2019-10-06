from django.db import models
from django.utils import timezone

# Create your models here.


class Visitor(models.Model):
    ip = models.GenericIPAddressField(
        unpack_ipv4=True, unique=True, blank=False, verbose_name="IP地址")
    first_time = models.DateTimeField(
        auto_now_add=True, verbose_name="首次访问时间")
    last_time = models.DateTimeField(
        auto_now=True, verbose_name="最后访问时间")
    count = models.IntegerField(default=1, verbose_name='访问次数')

    class Meta:
        verbose_name = "访问者"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.count += 1
        super(Visitor, self).save(*args, **kwargs)

    def __str__(self):
        return self.ip


class Soul(models.Model):
    title = models.CharField(max_length=300, blank=False, verbose_name="鸡汤")
    hits = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = "毒鸡汤"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
