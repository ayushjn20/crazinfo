# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_auto_20170605_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='description',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feed',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feed',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
