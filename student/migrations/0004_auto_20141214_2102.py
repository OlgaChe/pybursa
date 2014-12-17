# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_dossier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='package',
            field=models.CharField(default=b's', max_length=1, choices=[(b's', b'Standard'), (b'g', b'Gold'), (b'p', b'Platinum')]),
            preserve_default=True,
        ),
    ]
