# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0002_dossier_un_courses'),
        ('student', '0002_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dossier',
            field=models.OneToOneField(null=True, to='dossier.Dossier'),
            preserve_default=True,
        ),
    ]
