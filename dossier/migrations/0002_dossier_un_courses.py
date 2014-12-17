# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20141214_1757'),
        ('dossier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossier',
            name='un_courses',
            field=models.ManyToManyField(to='courses.Course', blank=True),
            preserve_default=True,
        ),
    ]
