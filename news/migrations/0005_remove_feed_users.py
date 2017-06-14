# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20170605_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='users',
        ),
    ]
