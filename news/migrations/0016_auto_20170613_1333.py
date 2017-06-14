# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20170612_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dp',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/news/static/images/'), null=True, upload_to=b'', blank=True),
        ),
    ]
