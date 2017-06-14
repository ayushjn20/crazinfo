# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0007_auto_20170605_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=256)),
                ('dp', models.ImageField(null=True, upload_to=b'')),
                ('phoneNo', models.CharField(max_length=12, null=True)),
                ('Bio', models.TextField(max_length=300, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='feed',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='feed',
            name='urlToImage',
            field=models.URLField(null=True),
        ),
    ]
