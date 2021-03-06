# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),

    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('technology', models.CharField(max_length=255, choices=[(b'p', b'Python'), (b'r', b'Ruby'), (b'j', b'JavaScript')])),
                ('venue', models.ForeignKey(related_name='cu_address', blank=True, to='address.Address', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
