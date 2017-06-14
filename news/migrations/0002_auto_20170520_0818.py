# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedFeeds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('decription', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=200)),
                ('urlToImage', models.CharField(max_length=200)),
                ('publishedAt', models.DateTimeField(verbose_name=b'News published at')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
