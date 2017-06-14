# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20170605_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='urlToImage',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
