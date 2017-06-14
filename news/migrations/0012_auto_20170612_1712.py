# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20170612_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
