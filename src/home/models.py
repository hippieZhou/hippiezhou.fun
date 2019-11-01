from django.db import models
from django.db.models.aggregates import Count
from django.utils import timezone
from random import randint
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


class SoulManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        if count > 0:
            random_index = randint(0, count - 1)
            return self.all()[random_index]
        else:
            return None


class Soul(models.Model):
    title = models.TextField(max_length=300, blank=False, verbose_name="鸡汤")
    hits = models.CharField(max_length=100, blank=False)

    objects = SoulManager()

    class Meta:
        verbose_name = "毒鸡汤"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
