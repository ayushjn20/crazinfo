# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20170613_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='source',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
