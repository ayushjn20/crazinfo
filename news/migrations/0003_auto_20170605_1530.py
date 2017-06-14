# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_auto_20170520_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('urlToImage', models.CharField(max_length=200)),
                ('publishedAt', models.DateTimeField(verbose_name=b'News published at')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reply', models.TextField()),
                ('key', models.ForeignKey(to='news.comment')),
                ('userkey', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='SavedFeeds',
        ),
        migrations.AddField(
            model_name='comment',
            name='key',
            field=models.ForeignKey(to='news.feed'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='userkey',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
