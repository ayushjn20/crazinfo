# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20170610_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
