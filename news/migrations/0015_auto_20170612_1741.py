# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20170612_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dp',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
