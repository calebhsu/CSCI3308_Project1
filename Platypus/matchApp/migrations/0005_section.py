# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchApp', '0004_auto_20150407_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('class_id', models.IntegerField(default=0)),
                ('section_number', models.IntegerField(default=0)),
                ('course_title', models.ForeignKey(to='matchApp.Course', null=True)),
            ],
        ),
    ]
