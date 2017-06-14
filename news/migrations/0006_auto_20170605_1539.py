# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_feed_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='author',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='publishedAt',
            field=models.DateTimeField(null=True, verbose_name=b'News published at'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
