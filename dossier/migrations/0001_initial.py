# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fav_color', models.CharField(default=b'r', max_length=1, choices=[(b'r', b'red'), (b'o', b'orange'), (b'y', b'yellow'), (b'g', b'green'), (b'w', b'white blue'), (b'b', b'blue'), (b'v', b'violet')])),
                ('address', models.ForeignKey(related_name='stu_address', blank=True, to='address.Address', null=True)),
                
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
