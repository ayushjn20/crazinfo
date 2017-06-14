# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(unique=True, max_length=10)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('password', models.CharField(unique=True, max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
