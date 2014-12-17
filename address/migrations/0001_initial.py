# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.CharField(max_length=8)),
                ('country', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25, blank=True)),
                ('region', models.CharField(max_length=25, blank=True)),
                ('street', models.CharField(max_length=25)),
                ('house', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
