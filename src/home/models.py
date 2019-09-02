from django.db import models
from datetime import datetime

# Create your models here.


class Visitor(models.Model):
    ip = models.GenericIPAddressField(
        unique=True, blank=False, verbose_name="IP地址")
    first_time = models.DateTimeField(
        default=datetime.now, verbose_name="首次访问时间")
    last_time = models.DateTimeField(
        default=datetime.now, verbose_name="最后访问时间")

    class Meta:
        verbose_name = "访问者"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.last_time = datetime.now
        super(Visitor, self).save(*args, **kwargs)

    def __str__(self):
        return self.ip
