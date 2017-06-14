# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0017_auto_20170613_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='userkey',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='userkey',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
