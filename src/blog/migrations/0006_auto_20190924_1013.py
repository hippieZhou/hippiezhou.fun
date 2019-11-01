# Generated by Django 2.2.5 on 2019-09-24 02:13

import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190920_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='正文支持 普通文本 和 MarkDown 格式', verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, max_length=250, unique_for_date='publish', verbose_name='别名'),
        ),
    ]
